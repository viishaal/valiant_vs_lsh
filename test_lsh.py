from data_generator import *
from algorithms import *
from utility import *

d = 500
epsilon = 0.5
vec_num = 1000
a_lsh = generate_random_matrix(d,vec_num)
points, v_lsh = generate_epsilon_close_pair(a_lsh, epsilon)

points = points.T
query = points
print "points:"
print points
print "d = %d" % d
print "#vectors = %d\n" % vec_num

k_set = [2,4]
L_set = [2,4,8]

# how many close points to find
neighbor_num = 1
#radius of hash family, larger w more points will be touched
LSH_family_w = 1.5* epsilon * d


lsh_tester = LSHtester(points, query, neighbor_num)
lsh_ans = lsh_tester.run(L1_norm, L1HashFamily(LSH_family_w, d), k_set, L_set)
bf = brute_force(points.T,1)
print "brute force answer: ", brute_force_pair(points.T,1)
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
		count += 1
