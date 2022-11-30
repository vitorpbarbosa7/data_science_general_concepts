#!/usr/bin/env python3

# following 
# https://towardsdatascience.com/understand-implement-logistic-regression-in-python-c1e1a329f460

import pandas as pd
import numpy as np 
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

def standardize_numeric_features(df) -> pd.DataFrame:
    df = df.copy()
    var_types = dict(X_train.dtypes != 'O')
    numeric_vars = [var for var, is_numeric in var_types.items() if is_numeric == True]
    for var in numeric_vars:
        var_mean = df[var].mean()
        var_std = df[var].std()
        df[var] = round((df[var] - var_mean) / var_std, 6)
    return df

df = pd.read_csv('titanic/train.csv')
df = df.dropna()
y_train = df['Survived']
X_train = df[['Pclass','Sex','Age']]

X_train_s = standardize_numeric_features(X_train)

X_train_s['Sex'] = X_train_s['Sex'].map({'male':0,'female':1})

print(X_train_s)

# add the constant term, if it was regression, it would be exactly the mean term
jpd = np.c_[np.ones(len(X_train_s)), np.array(X_train_s), np.array(y_train)]

# sigmoid
# z is theta0 + theta1*X1 + ... thetaN*XN
def sigmoid(log_odds):
	#log_odds is the commonly writen z parameter
	#the parameter which is in -infinity to +infinity range
	#log_odds = theta0*X0 + theta1*X1 + theta2*X2 + ... + thetaN*XN + 1
	predict_proba = 1 / (1 + np.exp(-log_odds))
	return predict_proba

n_epochs= 10
learning_rate = 0.1

# initialize arbitrary theta values
thetas = [0, 0, 0, 0]

# initialize lists to capture updating theta parameters after each epoch
theta0, theta1, theta2, theta3, log_likelihood_vals = [], [], [], [], []

# Initialize lists to capture updating theta parameters for every instance iteration in thie training set 
theta0_set, theta1_set, theta2_set, theta3_set, log_likelihood_set = [], [], [], [], []

for epoch in range(n_epochs):
	count = 0
	# chose to maximize the log_likelihood, instead of minimizing it
	log_likelihood = 0
	
	# for every row, every single input of covariates
	for single_sample in jpd:
		#calculation of log_odds for every instance
		log_odds = sum(thetas * single_sample[:4])
		# gets the probability from the log_odds value
		y_pred_proba = sigmoid(log_odds)
		y_actual = single_sample[-1]
		
		# gradient vector for each covariate
		# a derivada parcial para cada um dos covariates (each instance, each single_sample)
		# this complete derivative, can be found here : https://www.youtube.com/watch?v=0VMK18nphpg
		gradients = (y_actual - y_pred_proba) * single_sample[:4]
		
		# update parameters		
		thetas = thetas + (learning_rate * gradients)

		# maximize log_likelihood
		# we could choose to minimize the negative log likelihood function
		# all of this to obtain the MLE
		# the theta parameters are the estimates
		log_likelihood += y_actual * np.log(y_pred_proba) + (1 - y_actual) * np.log(1 - y_pred_proba)
		
		# capture intermediary attempts
		if count % 100 == 0:
			# print(f"log likelihood for sample: {log_likelihood}")	
			theta0_set.append(thetas[0])	
			theta1_set.append(thetas[1])	
			theta2_set.append(thetas[2])	
			theta3_set.append(thetas[3])
			log_likelihood_set.append(log_likelihood)	
		count += 1

	# at the end of each epoch, capture updated theta parameters			
	theta0.append(thetas[0])
	theta1.append(thetas[1])
	theta2.append(thetas[2])
	theta3.append(thetas[3])
	log_likelihood_vals.append(log_likelihood)

#print(f"theta0: {theta0}")
#print(f"theta1: {theta1}")
#print(f"theta2: {theta2}")
#print(f"theta3: {theta3}")
#print(f"log_likelihood_values: {log_likelihood_vals}")


x_axis = [i for i in range(1, 11)]
plt.figure(figsize=(14,6))
plt.title('Maximizing Log-Likelihood')
plt.xticks(x_axis)
plt.xlabel('epoch iteration')
plt.ylabel('log-likelihood')
plt.plot(x_axis, log_likelihood_vals, marker='o')
plt.tight_layout()
plt.show()





