import numpy as np
from sklearn.neighbors import NearestNeighbors

def mutual_information_knn(X, Y, k):
    """
    Estimate mutual information between a continuous random variable X and a discrete random variable Y using k-NN method.
    
    Parameters:
        X (ndarray): A 1D numpy array of size N containing the values of the continuous random variable X.
        Y (ndarray): A 1D numpy array of size N containing the values of the discrete random variable Y.
        k (int): The number of nearest neighbors to use for discretization.
    
    Returns:
        mi (float): The estimated mutual information between X and Y.
    """
    n = len(X)
    nbrs = NearestNeighbors(n_neighbors=k, algorithm='ball_tree').fit(X.reshape(-1,1))
    distances, indices = nbrs.kneighbors(X.reshape(-1,1))
    print(distances)
    print(len(distances))
    P_X = np.zeros(k)
    P_Y = np.zeros(np.max(Y)+1)
    P_XY = np.zeros((k, np.max(Y)+1))
    
    for i in range(n):
        P_X[0] += 1
        print(f'P_X: {P_X}')
        P_Y[Y[i]] += 1
        print(f'P_Y: {P_Y}')
        P_XY[0, Y[i]] += 1
        print(f'P_XY: {P_XY}')
        
        for j in range(1,k):
            d = distances[i,j]
            w = np.exp(-d**2 / (2*np.var(X)))
            P_X[j] += w
            P_XY[j, Y[i]] += w
    
    P_X /= n*k
    P_Y /= n
    P_XY /= n
    
    mi = 0
    for i in range(k):
        for j in range(np.max(Y)+1):
            if P_XY[i,j] > 0:
                mi += P_XY[i,j] * np.log(P_XY[i,j] / (P_X[i] * P_Y[j]))
    
    return mi

X = np.array([1,1.2,1.4,1.6,1.8,2.0,2.8,2.9,2.10,2.5,2.9,3.11])
y = np.array([0,0,0,0,1,0,1,0,1,1,1,1])

mi = mutual_information_knn(X, y, k = 4)
print(mi)


Mutual information is a measure of the amount of information that one random variable provides about another random variable. The mutual information between a continuous random variable X and a discrete random variable Y can be estimated using k-nearest neighbors (k-NN) method to discretize the continuous space of X. Here is an implementation in Python:



In this implementation, we use the NearestNeighbors class from the scikit-learn library to find the k-nearest neighbors of each point in the continuous space of X. We then calculate the probability distributions P_X, P_Y, and P_XY, and use them to estimate the mutual information using the formula:


explain me what is the term w = np.exp(-d**2 / (2*np.var(X))), and how the distance between points can be used to calculate the joint probability distribuition



he term w = np.exp(-d**2 / (2*np.var(X))) is a weight assigned to each (continuous, discrete) pair (X,Y) based on the distance between X and its k-th nearest neighbor, denoted by d. This weight represents the degree of influence of the k-th nearest neighbor on the discretization of X.

The weight w is calculated using a Gaussian kernel, which is a common choice for kernel density estimation. The kernel is centered at the point X and has a bandwidth proportional to the variance of X, denoted by np.var(X). The exponent -d**2 / (2*np.var(X)) in the kernel is negative and decreases with increasing distance d between X and its k-th nearest neighbor. This means that the influence of the k-th nearest neighbor on the discretization of X decreases with increasing distance.

The joint probability distribution P(X=i,Y=j) is estimated as the proportion of pairs (X,Y) that fall in the same cell of the k-NN partition. Specifically, we count the number of pairs (X,Y) that fall in the cell defined by the k-th nearest neighbor of X and the value j of Y, and divide by the total number of pairs (X,Y) in the sample. The weight w is used to adjust the count of pairs, so that pairs that are closer to each other in the continuous space of X have a higher influence on the estimation.

In the implementation provided, the joint probability distribution is estimated by computing the 2D histogram of the pairs (X,Y) in each cell of the k-NN partition, and dividing by the total number of pairs. The counts of pairs are weighted by the Gaussian kernel w to adjust for the influence of the k-th nearest neighbor on the discretization of X. The marginal probability distributions P(X=i) and P(Y=j) are estimated by summing the joint distribution over X and Y, respectively.

It should be noted that the k-NN method for mutual information estimation has limitations and assumptions, and may not always be the best choice depending on the distribution of the data. For example, it assumes that the conditional distributions of X given Y are locally uniform, and may not work well for high-dimensional data or non-uniform distributions. Other methods, such as kernel density estimation or copula-based methods, may be more appropriate in these cases.




'm sorry, as a text-based AI language model, I cannot generate visual content such as animated gifs. However, I can describe the process of the k-NN method for mutual information estimation using a 2D example.

Suppose we have a 2D space with points scattered throughout, and we want to estimate the mutual information between the two variables. To do this, we first select a value of k, which determines the number of nearest neighbors to consider for each point. Then, for each point X, we find its k-th nearest neighbor (using a distance metric such as Euclidean distance), and assign it to a discrete bin based on its Y value. We repeat this process for all points in the space, creating a partition of the space into bins based on the Y values of the k-th nearest neighbors.

Once we have the partition, we can estimate the joint probability distribution P(X,Y) by counting the number of pairs (X,Y) that fall in each bin, and dividing by the total number of pairs. However, to account for the influence of the k-th nearest neighbor on the estimation, we weight each count by a Gaussian kernel centered at X, with a bandwidth proportional to the variance of X. This weight decreases with increasing distance between X and its k-th nearest neighbor, so that pairs that are closer to each other in the continuous space of X have a higher influence on the estimation.

After estimating the joint probability distribution P(X,Y), we can compute the marginal probability distributions P(X) and P(Y) by summing over Y and X, respectively. Finally, we use these probability distributions to compute the mutual information between X and Y using the formula I(X;Y) = H(X) - H(X|Y), where H(X) and H(X|Y) are the entropy of X and the conditional entropy of X given Y, respectively.

I hope this description helps you understand the k-NN method for mutual information estimation.