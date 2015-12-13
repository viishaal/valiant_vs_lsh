from image_processing import *
from algorithms import *

dataset_indices = [4]

urls,points = read_imageNet(dataset_indices, (24, 18))
vec_num, d = points.shape

print "\nBrute Force"
print "===================================="
bf_result=brute_force(points.T,1)
print bf_result
print urls[bf_result[0][1][0]]
print urls[bf_result[0][1][1]]


print "\nLSH test"
print "===================================="
k_set = [2]
L_set = [2]
neighbor_num = 1
LSH_family_w = 550

lsh_tester = LSHtester(points, points, neighbor_num)
lsh_ans = lsh_tester.run(L1_norm, L1HashFamily(LSH_family_w, d), k_set, L_set)

c = 0
for k in k_set:
	for L in L_set:
		ans = lsh_ans[c]
		c+=1
		closest = [x[0] for x in ans]
		closest.sort(key=itemgetter(0))
		closest.reverse()
		result = closest[0]
		print "L%dk%d LSH result:" %(L,k)
		url1 = urls[result[1][0]]
		url2 = urls[result[1][1]]
		print result
		print url1
		print url2

print "\nvector aggregation test"
print "===================================="
vg = vector_aggregation(points.T, 0.33)
print vg
for pair in vg:
	print "similarity: %d" % pair[0]
	print urls[pair[1][0]]
	print urls[pair[1][1]]