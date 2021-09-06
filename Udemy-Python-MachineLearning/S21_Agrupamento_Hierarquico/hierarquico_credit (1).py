import matplotlib.pyplot as plt 
import numpy as np
import pandas as pd
from scipy.cluster.hierarchy import dendrogram, linkage 
from sklearn.cluster import AgglomerativeClustering  
from sklearn.preprocessing import StandardScaler

base = pd.read_csv('credit.csv', header = 1)

base['BILL_TOTAL'] = base.iloc[:,12:18].sum(axis=1)

X = base.iloc[:,[1,25]]
scaler = StandardScaler()
X = scaler.fit_transform(X)

dendrograma = dendrogram(linkage(X, method='ward'))
