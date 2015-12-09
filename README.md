Make sure you have numpy, matplotlib installed

For image processing, please make sure you have PIL, requests installed. There
is no need to download file for imageNet.

===========================================================
-Interesting result from running LSH on imageNet:

query: http://farm4.static.flickr.com/3201/2723160442_c6e464854b.jpg

brute-force result: http://farm2.static.flickr.com/1076/747117133_2224749aa6.jpg?v=1183820099

k2L2: http://farm1.static.flickr.com/165/361152965_46ab13ee6a.jpg

k2L4: = brute-force

k2L8: = brute-force

k4L2: http://farm4.static.flickr.com/3222/2774289885_6f595219ba.jpg

k4L4: = brute-force

k4L8: = brute-force

===========================================================

run test.py

Utility functions are in utility.py. 
Algorithms are in algorithms.py 
data_generator.py has functions which uses numpy to generate random matrix.
