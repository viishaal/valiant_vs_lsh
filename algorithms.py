# the suite of algorithms

# TODO: insert timers

import numpy as np
from utility import *
import math

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
	
	def __init__(self, hashFamily, k, L):
		super(LSH, self).__init__()
		self.hashFamily = hashFamily
		self.k = k
		self.L = 0
		self.hashTables = []
		self.fillHashTables(L)
	
	def fillHashTables(self, L):
		""" Fill or truncate hash tables """
		if L < self.L:
			self.hashTables = self.hashTables[:L]
		else:
			hashFunctions = []
			for l in xrange(self.L, L):
				# hash table l
				func = []
				for j in xrange(self.k):
					# h_j
					func.append(self.hashFamily.createHashFunction())
				hashFunctions.append(func)
			for h in hashFunctions:
				self.hashTables.append((h, defaultdict(lambda:[])))
	
	def hash(self, h, p):
		res = []
		for func in h:
			res.append(func.hash(p))
		return self.hashFamily.combine(res)
	
	def index(self, dataset):
		""" index points in dataset """
		self.dataset = dataset
		for h,table in self.hashTables:
			for i_x,p in enumerate(self.dataset):
				table[self.hash(h, p)].append(i_x)
		self.totalTouched = 0
		self.queryNum = 0
	
	def query(self, q, metric, resLimit):
		""" according to the metric, find resLimit closest points to q """
		uniqueClosePoints = set()
		for h,table in self.hashTables:
			closePoints = table.get(self.hash(h, q), [])
			uniqueClosePoints.update(closePoints)
		self.totalTouched += len(uniqueClosePoints)
		self.queryNum += 1
		tmp = []
		for i_x in uniqueClosePoints:
			tmp.append((i_x, metric(q, self.points[i_x])))
		uniqueClosePoints = tmp
		uniqueClosePoints.sort(key=itemgetter(1))
		return uniqueClosePoints[:resLimit]

	def getAverageTouched(self):
		return self.totalTouched/self.queryNum




# TODO: optimization multithreaded implementation and caches






