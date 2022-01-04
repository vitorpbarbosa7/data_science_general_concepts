import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

base = pd.read_csv('plano_saude2.csv')

X = base.iloc[:,0:1].values
Y = base.iloc[:,1].values

from sklearn.linear_model import LinearRegression
regressor1 = LinearRegression()
regressor1.fit(X, Y)
score1 = regressor1.score(X, Y)

figura1 = plt.figure(figsize = (3,3), dpi = 150)
plt.scatter(X, Y)
plt.plot(X, regressor1.predict(X), color='red')
plt.title('Regressão Linear Simples')
plt.xlabel('Idade')
plt.ylabel('Valor do convênio')
figura1.show()

#Regressão polinomial
from sklearn.preprocessing import PolynomialFeatures
poly = PolynomialFeatures(degree=2)
X_poly = poly.fit_transform(X)

regressor2 = LinearRegression()
regressor2.fit(X_poly, Y)
score2 = regressor2.score(X_poly, Y)

figura2 = plt.figure(figsize = (3,3), dpi = 150)
plt.scatter(X, Y)
plt.plot(X, regressor2.predict(X_poly), color='red')
plt.title('Regressão Polinomial de Segundo Grau')
plt.xlabel('Idade')
plt.ylabel('Valor do convênio')
figura2.show()

