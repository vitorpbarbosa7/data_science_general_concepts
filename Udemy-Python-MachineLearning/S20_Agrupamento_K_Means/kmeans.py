import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

#Tratar a base de dados com idade e salário
x = [20, 27, 21, 37, 46, 53, 55,47,52,32,39,41,39,48,48]
y = [200, 1200, 2900,1850,900,950,2000,2100,3000,5900,4100,5100,7000,5000,6500]

#É necessário trabalhar com arrays
base = np.array([x,y])
base = np.transpose(base)

#Pardonização dos dados
scaler = StandardScaler()
base = scaler.fit_transform(base)


#Único parâmetro obrigatório para passar é o número de clusters
kmeans = KMeans(n_clusters=3,
                init='k-means++',
                max_iter=300,
                n_init=10)

#Rodando o algoritmo
kmeans.fit(base)

#Variáveis para visualizar
centroides = kmeans.cluster_centers_
#São atribuídos rótulos de 0 a 2 para cada linha
rotulos = kmeans.labels_

#plt.scatter(base[:,0],base[:,1])
#plt.scatter(centroides[:,0],centroides[:,1], markersize = 15)

# String com as cores
cores = ['g.', 'r.', 'b.']

for i in range(len(base[:,0])):
    plt.plot(base[i][0], base[i][1], cores[rotulos[i]], markersize = 15)

plt.scatter(centroides[:,0], centroides[:,1], marker = 'x')
