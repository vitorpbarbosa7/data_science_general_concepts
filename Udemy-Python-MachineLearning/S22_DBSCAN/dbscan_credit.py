import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import DBSCAN

x=[20,  27,  21,  37,  46, 53, 55,  47,  52,  32,  39,  41,  39,  48,  48]  
y=[1000,1200,2900,1850,900,950,2000,2100,3000,5900,4100,5100,7000,5000,6500]  
plt.scatter(x,y)

base = np.array([x,y])

scaler = StandardScaler()
base = scaler.fit_transform(base)

#Modelo:
dbscan = DBSCAN(eps=0.5,
                min_samples=5,
                metric='euclidean', 
                algorithm='auto')

modelo = dbscan.fit(base)
