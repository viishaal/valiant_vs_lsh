# generates synthetic data for the light bulb test
import numpy as np
from utility import *
from algorithms import *
import time


def generate_random_matrix(rows, cols):
	""" returns a randomly generated +1,-1 numpy matrix
		given rows and cols of the resultant matrix
	"""
	s = rows * cols
	m =np.empty(shape=(1,s), dtype=np.int16)
	m = np.random.randint(2, size = s).reshape(rows, cols)
	m[m==0] = -1
	
	return m

def generate_epsilon_close_pair(m, epsilon):
	""" takes a numpy matrix, chooses a random column among set of all columns
		generates an epsilon close vector to the chosen vector, appends it to the matrix
	"""
	# randomly choose a column
	d = m.shape[0]
	total_cols = m.shape[1]
	random_idx = random_integer(total_cols)
	v1 = m[:, random_idx]

	# make a copy 
	v2 = np.copy(v1)

	# flip v2 values based on probability of epsilon/2
	thresh = epsilon/2.0
	v2[np.random.random(d) <= thresh] *= -1

	# append v2 to the matrix
	m = np.hstack((m, v2.reshape(d, 1)))
	shuffle_columns(m)
	return m, v2

