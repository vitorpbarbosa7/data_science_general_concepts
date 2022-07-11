# https://github.com/KacperKubara/ml-cookbook/blob/master/kmeans_and_gms/kmeans_and_gms.ipynb

from comparison import (
	create_dataset, 
	plot_dataset,
	plot_results,
	plot_different_gms
)
from sklearn.cluster import KMeans
from sklearn.mixture import GaussianMixture

data = create_dataset()
plot_dataset(data)

# Initialize KMeans and GaussianMixture models
kmeans = KMeans(n_clusters=3, 
                max_iter=1000,
                tol=1e-4)
gm = GaussianMixture(n_components=3, 
                     max_iter=1000, 
                     tol=1e-4,
                     init_params='random')

# Fit and predict the algorithms
y_kmeans = kmeans.fit_predict(data[:, :2])
y_gm = gm.fit_predict(data[:, :2])
y_gm_proba = gm.predict_proba(data[:, :2])

plot_results(data, y_kmeans, y_gm)


gm = GaussianMixture(n_components=3, 
                     max_iter=1000, 
                     tol=1e-4,
                     init_params='random')
gm_kmeans = GaussianMixture(n_components=3, 
                            max_iter=1000, 
                            tol=1e-4,
                            init_params='kmeans')

y_gm = gm.fit_predict(data[:, :2])
y_gm_proba = gm.predict_proba(data[:, :2])

y_gm_kmeans = gm_kmeans.fit_predict(data[:, :2])
y_gm_proba_kmeans = gm_kmeans.predict_proba(data[:, :2])

plot_different_gms(data, 0.34, 
                   y_gm, y_gm_proba, 
                   y_gm_kmeans, y_gm_proba_kmeans)
