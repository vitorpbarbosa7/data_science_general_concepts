import matplotlib.pyplot as plt
import numpy as np

_TRUE = 10
_FALSE = 90

ratio = _TRUE/_FALSE
print(ratio)

sqrt_ratio = np.sqrt(ratio)
print(sqrt_ratio)

inverse_ratio = _FALSE/_TRUE

low = sqrt_ratio
high = inverse_ratio

print('low is ',low, 'and high is ', high)


from scipy.stats import loguniform

r = loguniform.rvs(low, high)
plt.hist(r,density=True,bins='auto',histtype='stepfilled', alpha = 0.2)
plt.show()
