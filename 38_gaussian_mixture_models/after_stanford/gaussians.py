import matplotlib.pyplot as plt
import numpy as np

def gauss_2d(mu1,mu2, sigma1,sigma2,size:int = 100):
	x = np.random.normal(mu1,sigma1,size)
	y = np.random.normal(mu2,sigma2,size)
	return (x,y)

x, y = gauss_2d(2,1,0.3,0.5)
x2, y2 = gauss_2d(4,5,0.2,0.4) 
x = np.append(x,x2)
y = np.append(y,y2)
plt.scatter(x = x, y = y)
plt.show()
