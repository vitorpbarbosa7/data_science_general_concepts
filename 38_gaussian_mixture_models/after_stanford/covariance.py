import numpy as np 
from numpy import array as ar

matrix = ar([[1,2,3],[2,3,7]])

cov = np.cov(matrix)
print(cov)

a = np.diag(np.cov(matrix[0], matrix[0]))
b = np.diag(np.cov(matrix[1], matrix[1]))
c = np.cov(matrix[0],matrix[1])
d = np.cov(matrix[1],matrix[0])
print(a)

print(b)

print(c)

print(d)
	
	
