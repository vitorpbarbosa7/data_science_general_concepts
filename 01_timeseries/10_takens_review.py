# load some standard libraries
import numpy as np
import pandas as pd
import os
import math
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sklearn.neighbors import NearestNeighbors 
from IPython.display import display
from sklearn.feature_selection import mutual_info_classif

cityTable     = pd.read_csv('data/city_attributes.csv')
df_tem = pd.read_csv('data/temperature.csv', index_col=0)
df_tem.index = pd.to_datetime(df_tem.index)

def takensEmbedding(data, delay, dimension):
	'''
	'''
	if delay*dimension > len(data):
		raise NameError('Delay times dimension exceed length of data!')
	
	# cut last ones, according to desired delay and dimension values
	embeddedData = np.array([data[0:len(data)-delay*dimension]])

	# add new columns, according to delay and dimension values
	for i in range(1, dimension):
		embeddedData = np.append(embeddedData, [data[i*delay:len(data) - delay*(dimension - i)]], axis = 0)
	
	return embeddedData

time_range = pd.date_range(
				pd.to_datetime('22/06/2015', dayfirst = True),
				pd.to_datetime('31/08/2015', dayfirst = True),
				freq = 'H'
			)

weatherDataMontreal = df_tem.loc[time_range, 'Montreal']

# Making time series stationary to apply takensEmbeddingTheorem
windowSize = 24
lowPassFilteredSignal = weatherDataMontreal.rolling(windowSize, center = True).mean()
weatherDataMontreal = weatherDataMontreal - lowPassFilteredSignal
weatherDataMontreal = weatherDataMontreal.dropna()
embeddedWeather = takensEmbedding(weatherDataMontreal, delay = 5, dimension = 2);
print(len(embeddedWeather))

#Plot
fix, ax = plt.subplots(nrows=3, ncols = 1, figsize=(8,6));
ax[0].plot(weatherDataMontreal);
ax[1].plot(embeddedWeather[0,:], embeddedWeather[1,:]);
ax[2].axis('off')
plt.show()
