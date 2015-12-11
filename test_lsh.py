from data_generator import *
from algorithms import *
from utility import *

d = 50
vec_num = 200
a_lsh = generate_random_matrix(d,vec_num)
points, v_lsh = generate_epsilon_close_pair(a_lsh, 2)

points = points.T
query = points
print "points:"
print points
print "d = %d" % d
print "#vectors = %d\n" % vec_num

k_set = [2]
L_set = [2,4]

# how many close points to find
neighbor_num = 1
#radius of hash family, larger w more points will be touched
LSH_family_w = 15


lsh_tester = LSHtester(points, query, neighbor_num)
lsh_ans = lsh_tester.run(L1_norm, L1HashFamily(LSH_family_w, d), k_set, L_set)
#print lsh_ans
count = 0
for k in k_set:
	for L in L_set:
		print "L=%d, k=%d" %(L,k)
		ans = lsh_ans[count]
		closest = [x[0] for x in ans]
		closest.sort(key=itemgetter(0))
		closest.reverse()
		closest_pair = closest[0]
		print "closest pair: ",closest_pair
		bf = brute_force_pair(points.T,1)
		print "brute force answer: ", brute_force_pair(points.T,1)
		count += 1
