import numpy as np
from math import exp

def p(gamma):
	'''
	gamma = log_odds for gradient boosting classifier
	'''
	
	p = exp(gamma)/(1+exp(gamma))

	return p

gammas = [1.89,0.07,0.07]

ps = [p(gamma) for gamma in gammas]

print(ps) 
