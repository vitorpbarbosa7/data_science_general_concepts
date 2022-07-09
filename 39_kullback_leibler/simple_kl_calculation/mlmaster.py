#folling https://machinelearningmastery.com/divergence-between-probability-distributions/

# define distributions
from math import log2

events = ['red', 'green', 'blue']
p = [0.10, 0.40, 0.50]
q = [0.80, 0.15, 0.05]
r = [0.01,0.01,0.98]

def entropy(p):
	return sum(p[i]*log2(1/p[i]) for i in range(len(p)))

letters = ['P','Q','R']

for letter, dist in zip(letters,[p,q,r]):
	print(f'{letter} entropy is {entropy(dist)}')

# plot of distributions
from matplotlib import pyplot
# define distributions

def kl_divergence(p, q):
	return sum(p[i] * log2(p[i]/q[i]) for i in range(len(p)))

# calculate (P || Q)
kl_pq = kl_divergence(p, q)
print('KL(P || Q): %.3f bits' % kl_pq)

# calculate (Q || P)
kl_qp = kl_divergence(q, p)
print('KL(Q || P): %.3f bits' % kl_qp)

# calculate (R || Q)
kl_rq = kl_divergence(r, q)
print('KL(R || Q): %.3f bits' % kl_rq)

# calculate (Q || R)
kl_qr = kl_divergence(q, r)
print('KL(Q|| R): %.3f bits' % kl_qr)
