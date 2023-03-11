#!/usr/bin/env python3
import numpy as np 
from math import pi as pi
from math import exp as exp
import matplotlib.pyplot as plt
from functools import reduce

def likelihood_function(mean, sd, x):
	a = 1/(np.sqrt(2*pi*(sd**2)))
	b = exp(-((x-mean)**2)/(2*(sd**2)))
	normal_distribuition = a*b
	return normal_distribuition

sd = 2
x = 32
means = range(10, 50, 1)
sds = [sd]*len(means)
xs = [x]*len(means)

likelihood_values = []
for (mean, sd, x) in zip(means, sds, xs):
	likelihood_values.append(likelihood_function(mean, sd, x))

plt.scatter(x = means, y = likelihood_values)
plt.show()

def product_likelihood(mean, sd, distribuition:list):
	single_likelihood = []
	for point in distribuition:
		single_likelihood.append(likelihood_function(mean, sd, point))
	return reduce(lambda x, y: x*y, single_likelihood)	

distribuition = [32, 34]
products = []
for (mean, sd) in zip(means, sds):
	products.append(product_likelihood(mean, sd, distribuition))

plt.scatter(x = means, y = products)
plt.show()
