from math import log2
import matplotlib.pyplot as plt
import numpy as np

def entropy(p):
	return p*log2(1/p) + (1-p)*log2(1/(1-p))

entropy_values, probs = [], []
for p in np.arange(start = 0.01, stop = 0.99, step = 0.01):
	probs.append(p)
	entropy_values.append(entropy(p))

plt.scatter(x = probs, y = entropy_values)
plt.show()	
