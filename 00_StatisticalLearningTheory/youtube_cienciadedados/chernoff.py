import numpy as np
import matplotlib.pyplot as plt

ns = np.array(range(1,100000,1))
print(ns)
epsilon = 0.01

chernoff = [2*np.exp(-2*n*(epsilon)**2) for n in ns]

plt.scatter(x = ns, y = chernoff)
plt.show()
