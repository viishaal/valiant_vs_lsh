# utility timer functions, matrix computation functions
# please define a function here if you think it will be used often and by other developers
# this will enable easy debugging and factorized code

import numpy as np
import time
import heapq as hq
import matplotlib.pyplot as plt


def randomly_seed_numpy():
	""" seeds numpy randomizer with current unix timestamp
	"""
	np.random.seed(seed=int(time.time()))


def random_integer(h):
	""" returns random integer between [0,h) (note that h is exclusive)
		using numpy function
	"""
	return np.random.randint(0, h, size=1)[0]

def shuffle_columns(m):
	""" given a matrix randomly shuffles its columns
	"""
	np.random.shuffle(m.T)

def get_top_k(m, k=1):
	""" given a matrix iterates on its elements and maintains top k in a min heap

		return top k values with indices of element in matrix
		TODO: think about sketching to get top k heavy hitters in this sparse matrix
	"""
	rows = m.shape[0]
	cols = m.shape[1]
	i, j  = 0, 0
	h = []
	for i in range(0, rows):
		for j in range(0, cols):
			#ignore diagonal elements
			if i != j:
				elem = m[i,j]
				tup = (i, j)    # to track indexes of highest elements
				if len(h) < k:
					hq.heappush(h, (elem, tup))
				else:
					#print h, elem, i, j
					if h[0][0] < elem:
						hq.heappushpop(h, (elem, tup))
	return [hq.heappop(h) for i in range(0, len(h))]


def get_largest_element(m):
	""" returns largest element with its index in matrix
	"""
	rows = m.shape[0]
	cols = m.shape[1]
	i, j  = 0, 0
	largest = None
	largest_tup = None
	for i in range(0, rows):
		for j in range(0, cols):
			#ignore diagonal elements
			if i != j:
				elem = m[i,j]
				tup = (i, j)    # to track indexes of highest elements
				if largest < elem:
					largest = elem
					largest_tup = tup
	return [(largest, largest_tup)]

def flatten_matrix(m):
	""" given a nXn matrix m flattens it and removes diagonal elements from the flat
	"""
	arr = m.flat
	dim = m.shape[0]
	index = [i*dim+i for i in range(0,dim)]
	np.delete(arr, index)
	return arr


######################### matrix/array analysis

def matrix_to_histogram(m, bins=50, normed=1):
	""" plots a histogram to get general idea of distribution of off-diagonal elements
	"""
	arr = flatten_matrix(m)
	plt.hist(m, bins=bins, normed=normed)
	plt.show()














