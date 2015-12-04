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


# TODO: LSH
	
# TODO: optimization multithreaded implementation and caches






