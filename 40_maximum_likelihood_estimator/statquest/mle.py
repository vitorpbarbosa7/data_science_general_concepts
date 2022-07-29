#!/usr/bin/env python3
import numpy as np 
from math import pi as pi
from math import exp as exp
import matplotlib.pyplot as plt

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

plt.plot(likelihood_values)
plt.show()




