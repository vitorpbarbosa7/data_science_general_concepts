import numpy as np
from numpy import array as ar

def dist(a,b):
    dist = np.sqrt(np.sum((a - b)**2))
    return dist

def activation(dist, sigma):
    act = np.exp(-dist**2 / (2*(sigma**2)))
    return act

point_a = ar([1,2])

centroid = ar([2,2])

sigma = 1

distance = dist(point_a, centroid)
print(distance)

act = activation(distance, sigma)
print(act)

