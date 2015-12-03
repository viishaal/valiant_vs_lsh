from data_generator import *
from algorithms import *
from utility import *

#TODO make a python package

if __name__ == "__main__":
	randomly_seed_numpy()
	a = generate_random_matrix(3, 10)
	print a
	print generate_epsilon_close_pair(a, 2)
	print a.shape, a.ndim, a.dtype.name
	print brute_force(a, 1)
