# utility timer functions, matrix computation functions
# please define a function here if you think it will be used often and by other developers
# this will enable easy debugging and factorized code

import numpy as np
import time
import heapq as hq
import math
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

def get_top_k(m, k=1, diagonal_ignore = True):
	""" given a matrix iterates on its elements and maintains top k in a min heap
		diagonal_ignore => flag to indicate whether to ignore diagnoal elements or not
						   and search half the matrix assuming it is symmetric

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
			if diagonal_ignore and i <= j:
				continue;
			else:
				elem = m[i,j]
				tup = (i, j)    # to track indexes of highest elements
				if len(h) < k:
					hq.heappush(h, (elem, tup))
				else:
					#print h, elem, i, j
					if h[0][0] < elem:
						hq.heappushpop(h, (elem, tup))
	return [hq.heappop(h) for i in range(0, len(h))]


def get_largest_element(m, diagonal_ignore = True):
	""" returns largest element with its index in matrix
		diagonal_ignore => flag to indicate whether to ignore diagnoal elements or not
						   and search half the matrix assuming it is symmetric

	"""
	rows = m.shape[0]
	cols = m.shape[1]
	i, j  = 0, 0
	largest = None
	largest_tup = None
	for i in range(0, rows):
		for j in range(0, cols):
			if diagonal_ignore and i <= j:
				continue;
			else:
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

def generate_random_vector(n):
	""" given size of the vector returns a random numpy array of +1,-1
	"""
	v = np.random.randint(2, size = n)
	v[v==0] = -1
	return v

def randomly_partition_into_subsets(n, b):
	""" given n points/indexes randomly assigns them to b buckets
		returns mapping as a dictionary

		Note: points are indexed from 0 to n-1 and buckets from 0 to b-1

		TODO: check if each bucket should have exactly n/b elements or close enough will do
			  an approximation should yeild better run time
	"""
	mapping = {}
	available_buckets = range(0, b)  # all buckets are available initially
	remaining_points = False

	# uniformly distribute points to buckets now
	for i in range(0,n):
		no_available_buckets = len(available_buckets)
		if no_available_buckets == 0:   #all buckets filled exit
			remaining_points = True
			break

		r = random_integer(no_available_buckets)  # randomly generate a bucket index
		bucket_no = available_buckets[r]
		# add element to this bucket
		if bucket_no in mapping:
			mapping[bucket_no].append(i)
		else:
			mapping[bucket_no] = [i]

		# remove bucket from available list if it is filled
		if len(mapping[bucket_no]) == math.floor(n/b):
			available_buckets.remove(bucket_no)

	if remaining_points:   # still need to allocate points
		# generate random permutation
		pm = np.random.permutation(range(0,b))
		start = i
		for i in range(i, n):
			mapping[pm[i - start]].append(i)

	return mapping



######################### matrix/array analysis

def matrix_to_histogram(m, name="temp", bins=50, normed=1):
	""" plots a histogram to get general idea of distribution of off-diagonal elements
	"""
	arr = flatten_matrix(m)
	plt.hist(arr, bins=bins, normed=normed)
	plt.xlabel("Value")
	plt.ylabel("Frequency")
	plt.savefig(name)
	plt.show()






