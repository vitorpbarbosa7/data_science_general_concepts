import numpy as np 
import pandas as pd
import gc

class GMM:
	def __init__(self, n_components, max_iter = 100, comp_names=None):
		self.n_components = n_components
		self.max_iter = max_iter
		if comp_names == None:
			self.comp_names = [f"comp{index}" for index in range(self.n_components)]
		else:
			self.comp_names = comp_names
		
		# pi list contains the fraction of the dataset for every cluster
		self.pi = [1/self.n_components for comp in range(self.n_components)]

		print(len(self.pi))

	def fit(self, X):
		# Splitting the data in n_components sub-sets (zi clusters)
		new_X = np.array_split(X, self.n_components)
		
		# Initial computation of the mean-vector and covariance matrix
		self.mean_vector = [np.mean(X, axis = 0) for x in new_X]
		self.covariance_matrixes = [np.cov(X.T) for x in new_X]
		del new_X
		gc.collect()

		for iteration in range(self.max_iter):
			''' >> E - STEP << '''
			# Inicializando a matriz de probabilidades (r), ou como o Andrew Ng mostrava nas aulas de 
			# Stanford, as probabilidades wj de cada ponto pertencer a cada cluster

			self.w = np.zeros((len(X), self.n_components))

			# Calculating the probabilities matrix
			for n in range(len(X)):
				for k in range(self.n_components):
					self.w[n][k] = self.pi[k] * self.multivariate_normal(X[n], self.mean_vector[k], self.covariance_matrixes[k])
					self.w[n][k] /= sum([self.pi[j]*self.multivariate_normal(X[n], self.mean_vector[j], self.covariance_matrixes[j]) for j in range(self.n_components)])

					# class_prior = self.pi[k]
					# # each cluster with a mean and covariance matrix (distinct covariance matrix, 
					# #difference from Gaussian Discriminative Analysis
					# gaussian = self.multivariate_normal(X[n], self.mean_vector[k], self.covariance_matrixes[k])
					# print(type(gaussian))
					# print(type(class_prior))
					# particular_cluster_probability = gaussian*class_prior
					# intersection_probabilities = [self.pi[j]*self.multivariate_normal(X[n], self.mean_vector[j], self.covariance_matrixes[j]) for j in range(self.n_components)]
					# sum_all_probabilities = sum(intersection_probabilities)
					# result_prob = particular_cluster_probability/sum_all_probabilities
					# # print(result_prob)
					# self.w[n][k] = result_prob

			# Soma das probabilidades em cada feature
			N = np.sum(self.w, axis = 0)

			
			''' >> M - STEP << '''
			# A Partir das derivadas, dos valores de Phi, mu e sigma que maximizam a expressao das probabilidades
			# vamos atualizar os parametros

			# Médias
			self.mean_vector = np.zeros((self.n_components, len(X[0])))
			# Atualizar o vetor de médias de cada componente em cada feature
			for k in range(self.n_components):
				for n in range(len(X)):
					# Expected Value
					self.mean_vector[k] += self.w[n][k] * X[n]

			# N list - cada element como soma da correspondente coluna de w (probabilidades)
			print(f'N list: {N}')
			self.mean_vector = [(1/N[k])*self.mean_vector[k] for k in range(self.n_components)]

			# Matrix de covariâncias - atualizar
			self.covariance_matrixes = [np.zeros( (len(X[0]), len(X[0]) ) ) for k in range(self.n_components)]
			for k in range(self.n_components):
				self.covariance_matrixes[k] = np.cov(X.T, aweights = (self.w[:, k]), ddof = 0)
			self.covariance_matrixes = [(1/N[k])*self.covariance_matrixes[k]]

			# Class Prior probabilities update
			self.pi = [(N[k]/len(X) for k in range(self.n_components))]


	def multivariate_normal(self, X_row, mean_vector, covariance_matrix):
		d = X_row.shape[0]
		pi_const = 2*np.pi
		det_sigma = np.linalg.det(covariance_matrix)
		a_term = 1/(np.sqrt((pi_const**d)*det_sigma))

		inv_sigma = np.linalg.inv(covariance_matrix)
		x_mean_vector = (X_row - mean_vector)
		np_dot = np.dot(np.dot(x_mean_vector.T,inv_sigma),x_mean_vector)
		exp_term = np.exp((-1/2)*np_dot)

		single_probability = a_term*exp_term

		return single_probability
