from math import log2, log
import numpy as np
import matplotlib.pyplot as plt


def shattering_coefficient(R,p,n):
	'''

	General form:
	log N(F,n)/n

	for instance:
	log(n**2) will converge
	log(2**n) will not converge
	''' 
	
	
	shattering_coefficient = (R**2/p**2)*(log(n**2))
	
	return shattering_coefficient


def divergence_factor(R, p, n, c, delta):
	
	coefficients = shattering_coefficient(R, p, n)
	
	divergence_factor = np.sqrt((c/n)*(coefficients + log(1/delta)))

	return divergence_factor

def expected_risk(v_f:float,delta:float, R:float, p:float, n:int, c:float):
	'''
	delta: Good estimation for 1 - delta of cases. [0 - 1]
	v_f: Percentage of samples which lies within the margins
	'''

	expected_risk = v_f + divergence_factor(R, p, n, c, delta)

	return expected_risk


if __name__ == '__main__':
		
	R = 1
	p = 0.2
	c = 1
	delta = 0.05
	v_f = 0.01

	n_samples = range(1,10000)   
	
	expected_risks = [expected_risk(v_f, delta, R, p, n, c) for n in n_samples]
	
	plt.plot(expected_risks)
	plt.ylabel('expected_risk')
	plt.xlabel('number of samples')
	plt.show()
