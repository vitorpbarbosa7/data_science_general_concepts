import seaborn as sns
import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
from math import log2
from sklearn.datasets import load_iris
from sklearn.preprocessing import MinMaxScaler
from typing import Union, Dict, List


data = load_iris()
df = pd.DataFrame(data.data, columns=data.feature_names)
df['target'] = data.target

def select_sample_from_target(df:pd.DataFrame, target:Union[str, int]):
	first_sample = np.random.randint(
		low = 0, 
		high = df.shape[0], 
		size = int(df.shape[0]/2))

	df_one = df[df.index.isin(first_sample)]
	df_two = df[~df.index.isin(first_sample)]

	one = df_one[df_one['target']==target]
	two = df_two[df_two['target']==target]

	series_one = one.iloc[:,0]
	series_two = two.iloc[:,0]

	#scaler_one = MinMaxScaler()
	#scaler_scaler_two = MinMaxScaler()

	#scaler_series_one_norm = scaler_one.fit_transform(series_one.to_numpy().reshape(-1,1))
	#scaler_series_two_norm = scaler_two.fit_transform(series_two.to_numpy().reshape(-1,1))

	return series_one, series_two

def get_data_hist(data, bins = 5):
	count, bins_count = np.histogram(data, bins = bins)
	return count, bins_count

def get_pdf_cdf(count):
	pdf = count / sum(count)
	cdf = np.cumsum(pdf)
	return pdf, cdf

def plot_cdf_pdf(bins_count, pdf, cdf, cat:str = None):
	plt.plot(bins_count[1:], pdf, color = "red", label = f"pdf -{cat}")
	plt.plot(bins_count[1:], cdf, label = f"cdf - {cat}")
	plt.show()
	plt.legend()

def plot_single(data, cat:str = None):
	count, bins_count = get_data_hist(data)
	pdf, cdf = get_pdf_cdf(count)
	plot_cdf_pdf(bins_count, pdf, cdf, cat)

#Kullback-Leibler

def kl_divergence(p, q):
	return sum(p[i]*log2(p[i]/q[i]) for i in range(len(p)))

def get_pdf_cdf_from_data(data):
	count, bins_count = get_data_hist(data)
	pdf, cdf = get_pdf_cdf(count)
	return pdf, cdf 

def show_divergence(data_one, data_two):	
	pdf_one, _ = get_pdf_cdf_from_data(data_one)	
	pdf_two, _ = get_pdf_cdf_from_data(data_two)	
	
	kl = kl_divergence(pdf_one, pdf_two)
	print(f"kl divergence between samples is: {kl}")

a_zero, b_zero = select_sample_from_target(df, target = 0)
a_two, b_two = select_sample_from_target(df, target = 2)

#plot_single(a_zero, cat = '0')
plt.hist(a_zero)
plt.hist(b_zero)
plt.show()
plt.close()
show_divergence(a_zero, b_zero)



plt.hist(a_two)
plt.hist(a_zero)
plt.show()
plt.close()
show_divergence(a_two, a_zero)







