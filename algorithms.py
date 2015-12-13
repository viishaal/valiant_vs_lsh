# the suite of algorithms


import numpy as np
from utility import *
import heapq as hq
import math
import random
from collections import defaultdict
from operator import itemgetter
import time

########################################### Brutus

def brute_force(m, k=1):
	""" takes a matrix and calculates pairwise dot product of all columns
		returns k closest off-diagonal pairs indices and the value of dot products
		Ex return: [(v1, (i1,j1)), (v2, (i2,j2))] v1,v2 are values while (i1,j1), (i2,j2) are indices
	"""
	resultant_matrix = np.dot(m.T, m)
	if k == 1:
		return get_largest_element(resultant_matrix, True)
	else:
		return get_top_k(resultant_matrix, k, True)


def brute_force_disjoint(m1, m2, k=1):
	""" takes two matrices and calculates pairwise dot product of all columns
		returns k closest pairs indices and the value of dot products
		Ex return: [(v1, (i1,j1)), (v2, (i2,j2))] v1,v2 are values while (i1,j1), (i2,j2) are indices
	"""

	resultant_matrix = np.dot(m1.T, m2)
	if k == 1:
		return get_largest_element(resultant_matrix, False)
	else:
		return get_top_k(resultant_matrix, k, False)

def brute_force_pair(m,k=1):
	rows=m.shape[0]
	columns=m.shape[1]
	largest=None
	largest_tup=None
	if k==1:
		for i in range(0,columns):	
			for j in range(i+1,columns):
				dot=0
				for k in range(0,rows):
					dot+=m[k,i]*m[k,j]
				tup=(i,j)
				if largest < dot:
					largest=dot
					largest_tup=tup
		return [(largest,largest_tup)]
					
				
			
		
########################################### Valiant

def vector_aggregation(m, alpha, k=1):
	totaltime=0
	n = m.shape[1]    # number of points
	d = m.shape[0]	  # dimensions

	# check input
	if k > pow(n, 2*(1-alpha)):
		print "Invalid value of k"
		return None

	no_of_subsets = int(math.floor(pow(n, (1-alpha))))
	# hardcoded iterations for now for the data set size that we are tesing on
	iterations = 10

	# heap to store highest k elements
	h = []

	for i in range(0, iterations):
		# randomly partition points into subsets
		mapping = randomly_partition_into_subsets(n, no_of_subsets)

		W = []    # list of W matrix
		
		for j in range(0, iterations):
			# generate q to flip vectors randomly
			q = generate_random_vector(n)

			# create Z matrices
			
			Z = np.empty(shape = (d, no_of_subsets), dtype='int16') 
			#Z.astype(int32)
			for key in mapping:
				indices = mapping[key]
				Z[:, key] = np.sum((m[:, indices] * q[indices]), axis = 1)

			# TODO: replace with Strassens
			W.append(np.dot(Z.T, Z))

		# create the W matrix from the W list of matrices (75% percentile)
		W_percentile = np.empty(shape = (no_of_subsets, no_of_subsets))
		for x in range(0, no_of_subsets):
			for y in range(0, no_of_subsets):
				l = [W[ctr][x, y] for ctr in range(0, len(W))]
				W_percentile[x, y] = np.percentile(np.array(l), 75, interpolation='lower')
		
		# search for top k elements in W_percentile matrix
		if k == 1:
			top_k = get_largest_element(W_percentile, True)
		else:
			top_k = get_top_k(W_percentile, k, True)
	
		for elem in top_k:
			# get the corresponding buckets
			(b1, b2) = elem[1]
			# brute force search vectors in b1 and b2
			m1 = m[:, mapping[b1]]
			m2 = m[:, mapping[b2]]

			top_k_in_iteration = brute_force_disjoint(m1, m2, k)

			# store in heap
			for p in top_k_in_iteration:
				# reverse map p to original indexes in m
				val = p[0]
				idx1 = mapping[b1][p[1][0]]
				idx2 = mapping[b2][p[1][1]]
				if len(h) < k:
					hq.heappush(h, (val, (idx1, idx2)))
				elif h[0][0] < p[0]:
					hq.heappushpop(h, (val, (idx1, idx2)))
	return [hq.heappop(h) for i in range(0, len(h))]



def expand_and_aggregate(X, rho, tau, w, k=1):
	""" given an m x n matrix X, performs tensor embedding on X

	"""
	alpha = 1/(2 * (4 - w))
	m = X.shape[0]
	n = X.shape[1]

	# final dimension
	_m = math.floor(pow(n, 2 * alpha + math.log(rho, 2)/math.log(tau, 2)) * pow(math.log(n, 2), 4) )
	q = math.ceil(math.log(n, 2) / (-2 * math.log(tau, 2)))
	if q > m:
		q = m

	Y = np.empty(shape = (_m, n))
	if _m >= n:
		# TODO: brute force???
		pass
	else:
		for i in range(0, _m):
			# choose q rows uniformly at random from m
			t = np.random.randint(0, m, size=q)
			Y[i, :] = np.sum(X[t, :], axis = 0)

	#TODO: integrate with aggregation after figuring out some stuff and bit of refactoring
	return Y

	

########################################### Indyk LSH

class LSHmain:
	def __init__(self, hash_family, k, L):
		self.hash_family = hash_family
		self.k = k
		self.L = 0
		self.hash_tables = []
		self.fill_hash_tables(L)
	
	def fill_hash_tables(self, L):
		""" Fill or truncate hash tables """
		if L < self.L:
			self.hash_tables = self.hash_tables[:L]
		else:
			hash_functions = []
			for l in xrange(self.L, L):
				# hash table l
				func = []
				for j in xrange(self.k):
					# h_j
					func.append(self.hash_family.create_hash_function())
				hash_functions.append(func)
			for h in hash_functions:
				self.hash_tables.append((h, defaultdict(lambda:[])))
	
	def hash(self, h, p):
		res = []
		for func in h:
			res.append(func.hash(p))
		return self.hash_family.combine(res)
	
	def index(self, points):
		""" index points in dataset """
		self.points = points
		for h,table in self.hash_tables:
			for i_x,p in enumerate(self.points):
				table[self.hash(h, p)].append(i_x)
		self.total_touched = 0
		self.query_num = 0
	
	def query(self, q, metric, res_limit):
		""" according to the metric, find resLimit closest points to q """
		unique_close_points = set()
		for h,table in self.hash_tables:
			close_points = table.get(self.hash(h, q), [])
			unique_close_points.update(close_points)
		self.total_touched += len(unique_close_points)
		self.query_num += 1
		tmp = []
		for i_x in unique_close_points:
			tmp.append((i_x, metric(q, self.points[i_x])))
		unique_close_points = tmp
		unique_close_points.sort(key=itemgetter(1))
		return unique_close_points[:res_limit]

	def get_average_touched(self):
		return self.total_touched/self.query_num

class LSHtester:
	def __init__(self, points, queries, neighbor_num):
		self.points = points
		self.queries = queries
		self.neighbor_num = neighbor_num
	
	def run(self, metric, hash_family, k_set, L_set):
		"""
		metric: distance metric for NN
		hash_family: LSH hash family
		k_set: different k to try
		L_set: different L to try

		"""
		lsh_ans_set = []

		print("L\tk\t\ttouch\t\ttime")

		for k in k_set:
			lsh = LSHmain(hash_family, k, 0)
			for L in L_set:
				#preprocessing
				kL_set = []
				start_time = time.time()
				lsh.fill_hash_tables(L)
				lsh.index(self.points)
				#querying
				for q_i in xrange(len(self.queries)):
					q = self.queries[q_i]
					lsh_ans = []
					response = lsh.query(q, metric, self.neighbor_num+1)
					for i in xrange(1,len(response)):
						i_x,dist = response[i]
						lsh_ans.append((np.dot(self.queries[q_i], self.points[i_x]),(i_x,q_i)))
					kL_set.append(lsh_ans)
				end_time = time.time()
				lsh_ans_set.append(kL_set)
				print "{0}\t{1}\t\t{2:.2f}%\t\t{3:.4f} s".format(L, k,
						float(lsh.get_average_touched())*100/len(self.points),
						end_time - start_time)
		return lsh_ans_set

class L1HashFamily:
	def __init__(self, w, d):
		self.w = w
		self.d = d
	
	def create_hash_function(self):
		partition = self.random_partition()
		return L1Hash(partition, self.w)

	def random_partition(self):
		partition_set = []
		for i in xrange(self.d):
			partition_set.append(random.uniform(0, self.w))
		return partition_set
	
	def combine(self, hash_res_set):
		return str(hash_res_set)

class L1Hash:
	def __init__(self, S, w):
		self.S = S
		self.w = w
	
	def hash(self, vector):
		hash_res = []
		for i,s in enumerate(self.S):
			hash_res.append(int((vector[i]-s)/self.w))
		return str(hash_res)

def L1_norm(u, v):
	dist = np.subtract(u,v)
	return np.sum(np.absolute(dist))

# TODO: optimization multithreaded implementation and caches






