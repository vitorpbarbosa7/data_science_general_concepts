from math import log10
import numpy as np
import matplotlib.pyplot as plt

b = 100
a = 10
size = 100

diff = log10(b) - log10(a)

values = np.linspace(a,b,size)

pre_pdf = (1/diff)*(1/values)
pdf = pre_pdf/np.sum(pre_pdf)

plt.bar(x = values, height = pdf)
plt.show()


sampled = []
for i in range(10000):
	sampled.append(np.random.choice(a = values, p = pdf))

plt.hist(sampled)
plt.show()
