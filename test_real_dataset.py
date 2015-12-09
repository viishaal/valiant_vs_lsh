from image_processing import *
from algorithms import *

dataset_indices = [2,6]

urls,points = read_imageNet(dataset_indices, (24, 18))
vec_num, d = points.shape

print "\nLSH test"
print "===================================="
k_set = [2]
L_set = [2]
query_index = int(len(dataset_indices)/5)
neighbor_num = 1
LSH_family_w = 180

print "query image url: %s" % urls[query_index]

lsh_tester = LSHtester(points, [points[query_index]], neighbor_num)
ans_set,lsh_ans_set = lsh_tester.run(L1_norm, L1HashFamily(LSH_family_w, d), k_set, L_set)

for ans in ans_set:
	if len(ans) > 1:
		print "accurate match: %s" % urls[ans[1]]
c = 0
for k in k_set:
	for L in L_set:
		ans = lsh_ans_set[c]
		c+=1
		if len(ans) > 1:
			print "k={}, L={} ans: {}".format(k, L, urls[ans[1]]) 

print "\nvector aggregation test"
print "===================================="
vg = vector_aggregation(points.T, 0.33)
for pair in vg:
	print "similarity: %d" % pair[0]
	print urls[pair[1][0]]
	print urls[pair[1][1]]