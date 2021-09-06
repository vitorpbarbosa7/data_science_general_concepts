import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import DBSCAN

x=[20,  27,  21,  37,  46, 53, 55,  47,  52,  32,  39,  41,  39,  48,  48]  
y=[1000,1200,2900,1850,900,950,2000,2100,3000,5900,4100,5100,7000,5000,6500]  

plt.scatter(x,y)

base = np.array([x,y])
base = np.transpose(base)

basedf = pd.DataFrame(base)

scaler = StandardScaler()
base = scaler.fit_transform(base)

#Modelo:
#Foi realizada uma otimização manual por tentativa e erro de valores de 
#eps e de min_samples
dbscan = DBSCAN(eps=0.95,
                min_samples=2,
                metric='euclidean', 
                algorithm='auto')

dbscan.fit_predict(base)

previsoes = dbscan.labels_

cores = ['g.', 'r.', 'b.']

listaprevisoes = []

for i in range(len(base[:,0])):
    plt.plot(base[i][0], base[i][1], cores[previsoes[i]], markersize = 15)
    listaprevisoes.append(previsoes[i])
