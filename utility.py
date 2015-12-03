# utility timer functions, matrix computation functions
# please define a function here if you think it will be used often and by other developers
# this will enable easy debugging and factorized code

import numpy as np
import time


def randomly_seed_numpy():
	""" seeds numpy randomizer with current unix timestamp
	"""
	np.random.seed(seed=int(time.time()))


def random_integer(h):
	""" returns random integer between [0,h) (not h is exclusive)
		using numpy function
	"""
	return np.random.randint(0, h, size=1)[0]

def shuffle_columns(m):
	""" given a matrix randomly shuffles its columns
	"""
	np.random.shuffle(m.T)

