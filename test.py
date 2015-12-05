from data_generator import *
from algorithms import *
from utility import *

#TODO make a python package

if __name__ == "__main__":
	randomly_seed_numpy()
	a = generate_random_matrix(3, 10)
	print a
	m, v = generate_epsilon_close_pair(a, 2)
	#print a.shape, a.ndim, a.dtype.name
	print a.shape
	print m.shape
	print brute_force(m, 1)
	#matrix_to_histogram(np.dot(a.T, a), 10)

	print "vector aggregation"
	print vector_aggregation(m, 0.33)