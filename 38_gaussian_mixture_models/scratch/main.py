from gmm import GMM
from sklearn.datasets import make_blobs
import matplotlib.pyplot as plt
import numpy as np 

size = 1000
n_feat = 2
X, y = make_blobs(n_samples = size, n_features = n_feat)

# plt.scatter(x = X[:,0], y = X[:,1])
# plt.show() 

n_components = 2
gmm =  GMM(n_components, 100)
gmm.fit(X)

print(gmm.mean_vector)
print(gmm.covariance_matrixes)
print(gmm.pi)






# # Splitting the data in n_components sub-sets (zi clusters)
# new_X = np.array_split(X, n_components)

# # Initial computation of the mean-vector and covariance matrix
# mean_vector = [np.mean(X, axis = 0) for x in new_X]
# covariance_matrixes = [np.cov(X.T) for x in new_X]


# X_row = X[0]
# d = X.shape[1]
# pi_const = 2*np.pi
# det_sigma = np.linalg.det(covariance_matrixes[0])
# a_term = 1/(np.sqrt((pi_const**d)*det_sigma))

# inv_sigma = np.linalg.inv(covariance_matrixes[0])
# x_mean_vector = (X_row - mean_vector[0])
# np_dot = np.dot(np.dot(x_mean_vector.T,inv_sigma),x_mean_vector)
# exp_term = np.exp((-1/2)*np_dot)

# multivariate_gaussian = a_term*exp_term

# # gmm.multivariate_normal(X, mean_vector[0], covariance_matrixes[0])
