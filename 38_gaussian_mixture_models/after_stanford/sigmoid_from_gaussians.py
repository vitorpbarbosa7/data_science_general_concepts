import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

def gauss_2d(mu1,mu2, sigma1,sigma2,size:int = 10000):
	x1 = np.random.normal(mu1,sigma1,size)
	x2 = np.random.normal(mu2,sigma2,size)
	return (x1,x2)

mean_1 = 1
mean_2 = 2
sd_1 = 0.5
sd_2 = 0.5
x1, x2 = gauss_2d(mean_1,mean_2,sd_1,sd_2)
#plt.hist(x1)
#plt.hist(x2)
#plt.show()

all_points = np.append(x1,x2)
min_value = min(all_points)
max_value = max(all_points)
new_points = np.linspace(min_value, max_value, 1000)

probs_1 = stats.norm.pdf(new_points,mean_1,sd_1)*0.5

plt.scatter(x = new_points, y = probs_1)
plt.show()
