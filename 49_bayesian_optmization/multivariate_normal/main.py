import numpy as np 
import matplotlib.pyplot as plt 


a = 2
b = 40
c = 4
d = 42
xx = np.array([a,b])
yy = np.array([c,d])

mean_x = xx.mean()
mean_y = yy.mean()
std_xx = xx.std()
std_yy = yy.std()
means = [mean_x, mean_y]
std_x = std_xx/3
std_y = std_yy/3

corr = 0.7

covariance_crossed = std_x*std_y*corr

variance_x = std_x**2
variance_y = std_y**2

covs = [[variance_x, covariance_crossed],[covariance_crossed, variance_y]]
print(covs)

two_dimensional_gaussian = np.random.multivariate_normal(means, covs, 1000).T

plt.scatter(two_dimensional_gaussian[0], two_dimensional_gaussian[1])
plt.show();
