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

	#print "vector aggregation"
	#print vector_aggregation(m, 0.33)

	print "\nIndyk LSH"
	print "=========================="
	d = 500
	vec_num = 100
	a_lsh = generate_random_matrix(d,vec_num)
	points, v_lsh = generate_epsilon_close_pair(a_lsh, 2)
	points = points.T
	print "points:"
	print points
	print "d = %d" % d
	print "#vectors = %d\n" % vec_num

	#params
	k_set = [2,4]
	L_set = [2,4,8]
	query_size = vec_num/10
	# how many close points to find
	neighbor_num = 1
	#radius of hash family, larger w more points will be touched
	LSH_family_w = 280

	lsh_tester = LSHtester(points, points[:query_size], neighbor_num)
	ans, lsh_ans = lsh_tester.run(L1_norm, L1HashFamily(LSH_family_w, d), k_set, L_set)


