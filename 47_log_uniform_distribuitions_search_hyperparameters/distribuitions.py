# https://towardsdatascience.com/why-is-the-log-uniform-distribution-useful-for-hyperparameter-tuning-63c8d331698
from scipy.stats import loguniform, uniform
import numpy as np

import matplotlib.pyplot as plt
import seaborn as sns

LOWER = 0.0001
UPPER = 100
SIZE = 100

rv_loguniform = loguniform.rvs(LOWER, UPPER, size=SIZE)
rv_uniform = np.random.uniform(LOWER, UPPER, SIZE)

rv_1 = np.random.uniform(np.log10(LOWER), np.log10(UPPER), SIZE)

fix, ax = plt.subplots(2)
sns.histplot(data=rv_1, bins=20, ax=ax[0])
ax[0].set_title("Uniform distribution on the log-scale")
sns.histplot(data=10 ** rv_1, bins=20, ax=ax[1])
ax[1].set_title("Back to linear scale")
plt.show();

sum_1 = sum((rv_loguniform >= 0.0001) & (rv_loguniform < 0.001))
sum_2 = sum((rv_loguniform >= 0.001) & (rv_loguniform < 0.01))
sum_3 = sum((rv_loguniform >= 10) & (rv_loguniform < 100))

print(f"Number of values between 0.0001 and 0.001: {sum_1}")
print(f"Number of values between 0.001 and 0.01: {sum_2}")
print(f"Number of values between 10 and 100: {sum_3}")

