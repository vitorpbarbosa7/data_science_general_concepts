import matplotlib.pyplot as plt
import numpy as np 

proba1, proba0 = [], []
log_odds = [i for i in range(-10, 11)]

for instance in log_odds:
	p1 = 1/(1 + np.exp(-instance)) 
	p0 = 1 - p1
	proba1.append(p1)
	proba0.append(p0)

print(proba1)
print(proba0)

plt.figure(figsize=(12,6))
plt.plot(log_odds, proba1, marker='.', label='predict proba 1')
plt.show()
