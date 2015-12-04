# the suite of algorithms

# TODO: insert timers

import numpy as np
from utility import *
import math
from collections import defaultdict
from operater import itemgetter

########################################### Brutus

def brute_force(m, k=1):
	""" takes a matrix and calculates pairwise dot product of all columns
		returns k closest pairs indices and the value of dot products
	"""
	resultant_matrix = np.dot(m.T, m)
	if k == 1:
		return get_largest_element(resultant_matrix)
	else:
		return get_top_k(resultant_matrix, k)


########################################### Valiant

def vector_aggregation(m, alpha, k):
	# check input
	if k > pow(n, 2(1-alpha)):
		print "Invalid value of k"
		return None

	n = m.shape[1]    # number of points
	d = m.shape[0]	  # dimensions
	iterations = 10 * int(math.log(n, 2))     # 10logn
	no_of_subsets = math.floor(pow(n, (1-alpha)))
	for i in range(0, iterations):
		# randomly partition points into subsets
		mapping = randomly_partition_into_subsets(n, no_of_subsets)

		W = []    # list of W matrix
		for j in range(0, iterations):
			# generate q to flip vectors randomly
			q = generate_random_vector(n)

			# create Z matrices
			Z = np.empty(shape = (d, no_of_subsets)) 
			for key in mapping:
				indices = mapping[key]
				Z[:, key] = np.sum((m[:, indices] * q[indices]), axis = 1)
				W.append(np.dot(Z.T, Z))


def expand_and_aggregate():
	pass

###########################################Indyk LSH
# TODO: LSH
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
	
	def index(self, dataset):
		""" index points in dataset """
		self.dataset = dataset
		for h,table in self.hash_tables:
			for i_x,p in enumerate(self.dataset):
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
		close_points_ans = []
		for q in queries:
			res = []
			for i_x,dist in self.brute_force_search(q, metric,
					self.neighbor_num+1):
				res.append(i_x)
			close_points_ans.append(res)

		print("L\tk\tacc\ttouch")

		for k in k_set:
			lsh = LSHmain(hash_family, k, 0)
			for L in L_set:
				lsh.resize(L)
				lsh.index(self.points)

				right_points = 0
				
				for q,ans in zip(self.queries, close_points_ans):
					lsh_ans = []
					for i_x,dist in lsh.query(q, metric,
							self.neighbor_num+1):
						lsh_ans.append(i_x)
					if lsh_ans == ans:
						right_points += 1
				print "{0}\t{1}\t{2}\t{3}".format(L, k,
						float(right_points)/100,
						float(lsh.get_average_touched())/len(self.points))
	
	def brute_force_search(self, q, metric, res_limit):
		""" brute force search for close points """
		close_points = []
		for i_x,p in enumerate(self.points):
			close_points.append((i_x, metric(p, q)))
		return sorted(close_points, key=itemgetter(1))[:res_limit]



# TODO: optimization multithreaded implementation and caches






