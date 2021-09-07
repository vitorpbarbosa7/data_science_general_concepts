import matplotlib.pyplot as plt 
import numpy as np
from scipy.cluster.hierarchy import dendrogram, linkage 
from sklearn.cluster import AgglomerativeClustering  
from sklearn.preprocessing import StandardScaler

x = [20, 27, 21, 37, 46, 53, 55, 47, 52 ,32, 39, 41, 39, 48, 48]
y = [1000, 12000, 2900, 1850, 900, 950, 1000, 2100, 3000, 5900, 4100, 5100, 7000, 5000 ,6500]

plt.scatter(x,y)

base = np.array([x,y])
base = np.transpose(base)

#Escalonamento
scaler = StandardScaler()
base = scaler.fit_transform(base) 

#Criação da variável dendrograma
dendrograma =  dendrogram(linkage(base, method='ward'))
plt.title('Dendrograma')
plt.xlabel('Pessoas')
plt.ylabel('Distância Euclidiana')

hc = AgglomerativeClustering(n_clusters=3, 
                             affinity='euclidean',
                             linkage='ward')

previsoes =  hc.fit_predict(base)

#Cá está o gráfico
cores = ['red','orange','green']
rotulos = ['C1','C2','C3']
for i in range(0,len(cores)):
    plt.scatter(base[previsoes == i, 0], base[previsoes ==i, 1],  c = cores[i], label = rotulos[i])
plt.xlabel('Idade')
plt.ylabel('Salário')
plt.legend()
