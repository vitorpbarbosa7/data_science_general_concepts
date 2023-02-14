import numpy as np
from numpy import array as ar
import matplotlib.pyplot as plt

def max_leaves(depth:int = 2):
	
	max_leaves = 2**(depth)
	
	return max_leaves


depths = list(range(2,8,1))
leaves = [max_leaves(depth) for depth in depths]

plt.scatter(x = depths, y = leaves)
plt.show()
