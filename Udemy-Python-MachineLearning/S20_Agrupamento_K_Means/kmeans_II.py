import numpy as np 
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

#Importar um dataset específico
from sklearn.datasets import make_blobs

#x são os registros e y os clusters
x, y = make_blobs(n_samples = 1000, 
                  centers = 5)

#Plot:
plt.scatter(x[:,0], x[:,1])

#Utilizar efetivamente o KMeans
#x são os registros e y os clusters
kmeans = KMeans(n_clusters=5)
kmeans.fit(x) 
 
#Verificar se está colocando os dados nos grupos certos
previsoes = kmeans.predict(x)

#Plotra com os clusters do KMeans
#Previsoes é constituída por números inteiros, interessante, ele pega
plt.scatter(x[:,0],x[:,1],c = previsoes)
