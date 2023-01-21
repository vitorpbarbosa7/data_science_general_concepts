from math import log2
import numpy as np
import matplotlib.pyplot as plt


def shattering_coefficient(R,p,n):
	
	shattering_coefficient = (R**2/p**2)*(log2(n)**2)
	
	return shattering_coefficient

R = 1
p = 0.99

n_samples = range(1,10000)

coefficients = [shattering_coefficient(R,p,n) for n in n_samples]

plt.plot(coefficients)
plt.ylabel('shattering coefficient')
plt.xlabel('number of samples')
plt.show()
