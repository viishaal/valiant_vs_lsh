from image_processing import *
from algorithms import *

urls,points = read_imageNet((408100,408200), (24, 18))
vec_num, d = points.shape
k_set = [2,4]
L_set = [2,4,8]
query_size = 3
query_index = 50
neighbor_num = 1
LSH_family_w = 80

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