import matplotlib.pyplot as plt 
import numpy as np
import pandas as pd
from scipy.cluster.hierarchy import dendrogram, linkage 
from sklearn.cluster import AgglomerativeClustering  
from sklearn.preprocessing import StandardScaler

base = pd.read_csv('credit.csv', header = 1)

