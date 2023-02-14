from math import log, exp
import matplotlib.pyplot as plt

values = list(range(1,100,1))
inverse_values = sorted(values, reverse=True)

combination = list(zip(values,inverse_values))

def odd_calc(a,b):
	return a/b

def log_odd(a,b):
	odd = odd_calc(a,b)
	log_odd = log(odd)
	return log_odd

def logistic(a,b):
	log_odd_value = log_odd(a,b)
	numerator = exp(log_odd_value)
	denominator = 1 + exp(log_odd_value)
	res = numerator/denominator

	return res

log_odds = [log_odd(a,b) for a,b in combination]
probs = [logistic(a,b) for a,b in combination]

fig, ax = plt.subplots(2)
ax[0].scatter(x = values, y = log_odds)
ax[1].scatter(x = values, y = probs)
plt.show()
