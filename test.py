from data_generator import *
from algorithms import *
from utility import *

#TODO make a python package
"""
if __name__ == "__main__":
	randomly_seed_numpy()
	a=generate_random_matrix(1000,100000)
	m, v = generate_epsilon_close_pair(a, 0)
	#print vector_aggregation(m,0.33)
	#print brute_force_pair(m,1)
	"""
"""	for i in [10, 100]:
		for j in [100,1000,10000]:
			print i, j
			a = generate_random_matrix(i, j)
			print a
			m, v = generate_epsilon_close_pair(a, 0)
	#m=a
	#print a.shape, a.ndim, a.dtype.name
		#print a.shape
		#print m.shape
			start=time.time()
			print brute_force(m, 1)
			end=time.time()
			print end-start
	#matrix_to_histogram(np.dot(a.T, a), 10)

	#print "vector aggregation"
			start=time.time()
			print vector_aggregation(m, 0.33)
			end=time.time()
			print end-start
"""
if __name__ == "__main__":
	randomly_seed_numpy()
	for i in [10, 50, 100, 500, 1000]:
		for j in [1000, 5000, 10000, 50000, 100000]:
			if i*50<=j:			
				a=generate_random_matrix(i,j)
				m, v = generate_epsilon_close_pair(a, 0);
				print "Dimensions:",i, "Points:",j
				start=time.time()
				result=brute_force_pair(m,1)
				end=time.time()
				print "Brute force result:" , result
				print "Time=",(end-start)
				count=0
				for k in range(10):
					start=time.time()
					result=vector_aggregation(m,0.33)
					end=time.time()
					print "Vector aggregation result",k,":",result
					print "Time=",(end-start)
					if result[0][0] == i :
						count+=1
				print "Vector aggregation accuracy:",count*10,"%"
	
	"""
	print "\nIndyk LSH"
	print "=========================="
<<<<<<< Updated upstream
=======
<<<<<<< HEAD
	d = 1000
	vec_num = 100000
#	a_lsh = generate_random_matrix(d,vec_num)
	a_lsh=a
#	points, v_lsh = generate_epsilon_close_pair(a_lsh, 0.2)
	points=m
	v_lsh=v
=======
>>>>>>> Stashed changes
	d = 500
	vec_num = 100
	a_lsh = generate_random_matrix(d,vec_num)
	points, v_lsh = generate_epsilon_close_pair(a_lsh, 2)
>>>>>>> 289a56c65ff78f67df5b16952cce7b213eb851ff
	points = points.T
	print "points:"
	print points
	print "d = %d" % d
	print "#vectors = %d\n" % vec_num

	#params
<<<<<<< Updated upstream
=======
<<<<<<< HEAD
	k_set = [2,4,8]
	L_set = [2,4,8,16]
	query_size = 1
=======
>>>>>>> Stashed changes
	k_set = [2,4]
	L_set = [2,4,8]
	query_size = vec_num/10
>>>>>>> 289a56c65ff78f67df5b16952cce7b213eb851ff
	# how many close points to find
	neighbor_num = 1
	#radius of hash family, larger w more points will be touched
	LSH_family_w = 280

	lsh_tester = LSHtester(points, points[:query_size], neighbor_num)
<<<<<<< Updated upstream
=======
<<<<<<< HEAD
	lsh_tester.run(L1_norm, L1HashFamily(LSH_family_w, d), k_set, L_set)
"""
	ans, lsh_ans = lsh_tester.run(L1_norm, L1HashFamily(LSH_family_w, d), k_set, L_set)


