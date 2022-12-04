# trying to understand the Box Kernel estimation from this video 
# https://www.youtube.com/watch?v=aDlv5rn0938

import numpy as np 
from math import log2
from sklearn.metrics import mutual_info_score

x = [1,2,3,4,5,6,7,8,8,9,10,11]
y = [0.5,1,1.5,2,3,3,3,4,5,6,7,8]
z = list(zip(x,y))
r = 1.3

print(len(x), len(y))

def norm(a,b):
	
	x = (a[0] - b[0])**2
	y = (a[1] - b[1])**2

	norm = np.sqrt(x + y)
	
	return norm

def box_kernel(distance, distance_limit):
	if distance > distance_limit:
		return 0
	else:
		return 1

within_radius = {}
for i in range(len(z)-1):
	booleans = []
	for j in range(len(z)-1):
		calculated_norm = np.round(norm(z[i],z[j]),4)
		booleans.append(box_kernel(calculated_norm, r))
	
	within_radius[i] = booleans	

print(within_radius)

probability_of_point_near = {}
N = len(z)
for point, distances in within_radius.items():
	
	probability_of_point_near[point] = np.round(np.mean(distances),4)

print(probability_of_point_near)

fxy = {}
for point, single_point_near in probability_of_point_near.items():
	
	fxy[point] = single_point_near/2*r

print(fxy)

entropy = 0
for _, fxy in fxy.items():
	entropy += log2(fxy)
	
entropy = entropy/N

print(entropy)
	
print(mutual_info_score(x,y))
