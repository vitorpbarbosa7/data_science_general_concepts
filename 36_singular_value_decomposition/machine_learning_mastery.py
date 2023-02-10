from numpy import array
from scipy.linalg import svd

from numpy import dot 
from numpy import zeros
from numpy import diag

A = array([[1,2], [3,4], [5,6]])

u, s, vt = svd(A)

print(u)

print(s)

print(vt)

sigma = zeros((A.shape[0], A.shape[1]))

sigma[:A.shape[1], :A.shape[1]] = diag(s)

u.dot(sigma.dot(vt))

# Data Reduction

A = array([
	[1,2,3,4,5,6,7,8,9,10],
	[11,12,13,14,15,16,17,18,19,20],
	[21,22,23,24,25,26,27,28,29,30]])

print(A)

# Singular-value decomposition
U, s, VT = svd(A)
# create m x n Sigma matrix
Sigma = zeros((A.shape[0], A.shape[1]))
# populate Sigma with n x n diagonal matrix
Sigma[:A.shape[0], :A.shape[0]] = diag(s)
# select
n_elements = 2
Sigma = Sigma[:, :n_elements]
VT = VT[:n_elements, :]
# reconstruct
B = U.dot(Sigma.dot(VT))
print(B)

# transform
T = U.dot(Sigma)
print(T)

T = A.dot(VT.T)
print(T)

## scikit-learn implementation

from sklearn.decomposition import TruncatedSVD
# define array
A = array([
	[1,2,3,4,5,6,7,8,9,10],
	[11,12,13,14,15,16,17,18,19,20],
	[21,22,23,24,25,26,27,28,29,30]])
print(A)
# svd
svd = TruncatedSVD(n_components=2)
svd.fit(A)
result = svd.transform(A)
print(result)


