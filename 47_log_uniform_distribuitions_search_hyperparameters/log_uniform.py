import numpy as np
from math import log
import matplotlib.pyplot as plt

def log_uniform(a,b,size):

	x =  np.linspace(a,b,size)
	diff = log(b) - log(a)
	res = 1/(x*diff)
	return x, res

a = 3
b = 10
size = 50
x, pdf = log_uniform(a,b,size)

print(pdf)

plt.bar(x = x, height = pdf)
plt.show()

