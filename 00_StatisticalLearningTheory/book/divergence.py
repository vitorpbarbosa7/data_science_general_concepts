import numpy as np 
import matplotlib.pyplot as plt

divergences = np.linspace(0.001, 1, 500)

def sample_est(epsilon, divergence):
	sample_size = (1/epsilon)*(1/divergence)
	return sample_size

EPS = 0.001
sample_sizes = []
for divergence in divergences:
	sample_sizes.append(sample_est(EPS, divergence))


plt.scatter(x = divergences, y = sample_sizes)
plt.show()
