# the suite of algorithms

import numpy as np
from utility import *

def brute_force(m, k=1):
	""" takes a matrix and calculates pairwise dot product of all columns
		returns k closest pairs indices and the value of dot products
	"""
	resultant_matrix = np.dot(m.T, m)
	if k == 1:
		return get_largest_element(resultant_matrix)
	else:
		return get_top_k(resultant_matrix, k)


# TODO: Valiant

# TODO: LSH
	
# TODO: optimization multithreaded implementation and caches