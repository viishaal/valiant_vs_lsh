from data_generator import *
from algorithms import *
from utility import *

#TODO make a python package

if __name__ == "__main__":
	randomly_seed_numpy()
	k_set = [2]
	L_set = [2]
	for i in [10, 50, 100, 500, 1000]: #d
		for j in [10000, 50000, 100000]: #n
			if i*50<=j:			
				a=generate_random_matrix(i,j)
				m, v = generate_epsilon_close_pair(a, 2);
				print "Dimensions (d):",i, "Points (n):",j
				start=time.time()
				bf_result=brute_force_pair(m,1)
				end=time.time()
				print "Brute force result:" , bf_result
				print "Time=",(end-start)
				print "=============================="
				va_count=0
				lsh_count_set = dict()
				for k in range(10):
					start=time.time()
					result=vector_aggregation(m,0.33)
					end=time.time()
					print "Vector aggregation:"
					print "result",k,":",result
					print "Time=",(end-start)
					if result[0][0] == bf_result[0][0] :
						va_count+=1
					print "LSH:"
					lsh_w = i/2
					points = m.T
					lsh_tester = LSHtester(points, points, 1)
					lsh_ans = lsh_tester.run(L1_norm, L1HashFamily(lsh_w, i), k_set, L_set)
					idx = 0
					for K in k_set:
						for L in L_set:
							key = "".join([str(K),str(L)])
							ans = lsh_ans[idx]
							closest = [x[0] for x in ans]
							closest.sort(key=itemgetter(0))
							closest.reverse()
							result = closest[0]
							print "L%dk%d LSH result %d: %d" %(L,K,k,result[0])
							if result[0] == bf_result[0][0]:
								if key in lsh_count_set:
									lsh_count_set[key] += 1
								else:
									lsh_count_set[key] = 1
							idx += 1
					print "=============================="

				print "Vector aggregation accuracy:",va_count*10,"%"
				for K in k_set:
					for L in L_set:
						key = "".join([str(K),str(L)])
						print "L{0}k{1} LSH accuracy: {2}%\n".format(L,K,lsh_count_set[key]*10),


