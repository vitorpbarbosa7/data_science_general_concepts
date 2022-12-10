# https://jamesmccaffrey.wordpress.com/2021/07/13/jensen-shannon-distance-example/

import numpy as np 
from scipy.spatial import distance
from math import log2

def KL(p,q):
	'''
	Computes the Kullback Leibler Divergence between two
	probability distribuitions, p and q

	Parameters:
	------------
	p, q : Probability distribuitions
	'''
	
	summation = 0
	for i in range(len(p)):
		summation += p[i] * np.log2(p[i]/q[i])

	return summation


def JS(p, q):
	
	# mean of distribuitions	
	m = 0.5 * (p + q)
 
	left = KL(p,m)
	right = KL(q,m)

	return np.sqrt((left + right) / 2)

def main():
	
	q = np.array([0.36, 0.48, 0.16], dtype = np.float32)
	p = np.array([0.3, 0.5, 0.2], dtype = np.float32)

	js_pq = JS(p,q)
	js_qp = JS(q,p)

	print(js_pq)
	print(js_qp)

if __name__ == "__main__":
	main()
