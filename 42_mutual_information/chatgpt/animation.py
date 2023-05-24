import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Generate random data
np.random.seed(123)
n = 100
X = np.random.normal(size=n)
Y = np.random.normal(size=n)

# Define the number of nearest neighbors to consider
k = 5

# Define the number of bins for Y
nbins = 10

# Create the partition of the space into bins
bins = np.linspace(np.min(Y), np.max(Y), nbins+1)
knn_bins = np.digitize(Y, bins)

# Initialize the figure and axes
fig, ax = plt.subplots()
ax.set_xlim(np.min(X), np.max(X))
ax.set_ylim(np.min(Y), np.max(Y))

# Initialize the scatter plot and histogram
scatter = ax.scatter(X, Y, c=knn_bins, cmap='viridis')
hist, _ = np.histogram(Y, bins=bins)

# Define the update function for the animation
def update(frame):
    # Get the k-th nearest neighbors for each point in X
    distances = np.abs(X[:, np.newaxis] - X)
    knn_indices = np.argpartition(distances, k+1, axis=1)[:, 1:k+1]
    knn_values = Y[knn_indices]

    # Calculate the weights using the Gaussian kernel
    weights = np.exp(-distances**2 / (2*np.var(X)))
    weights /= np.sum(weights, axis=1, keepdims=True)
    knn_weights = weights[:, knn_indices]

    # Estimate the joint probability distribution
    joint_prob = np.zeros((nbins, n))
    for i in range(nbins):
        in_bin = knn_bins == i+1
        joint_prob[i] = np.sum(knn_weights[:, in_bin], axis=1)

    # Estimate the marginal probability distributions
    marg_prob_X = np.sum(joint_prob, axis=0) / n
    marg_prob_Y = hist / n

    # Calculate the mutual information
    H_X = -np.sum(marg_prob_X * np.log(marg_prob_X))
    H_X_given_Y = np.sum(joint_prob / np.sum(joint_prob, axis=0, keepdims=True) * np.log(joint_prob / np.sum(joint_prob, axis=0, keepdims=True)))
    mutual_info = H_X - H_X_given_Y

    # Update the scatter plot and histogram
    scatter.set_offsets(np.column_stack((X, Y)))
    scatter.set_array(knn_bins)
    hist, _ = np.histogram(Y, bins=bins, weights=knn_weights.sum(axis=1))
    ax.collections[-1].set_height(hist)

    # Update the title with the mutual information
    ax.set_title(f'Mutual Information = {mutual_info:.3f}')

    return scatter, ax.collections[-1]

# Create the animation and save as a gif
ani = animation.FuncAnimation(fig, update, frames=100, interval=100)
ani.save('knn_mutual_info.gif', writer='pillow')
