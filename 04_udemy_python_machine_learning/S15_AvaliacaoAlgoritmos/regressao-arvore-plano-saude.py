import pandas as pd

base = pd.read_csv('plano_saude2.csv')

X = base.iloc[:, 0:1].values
Y = base.iloc[:, 1].values

from sklearn.tree import DecisionTreeRegressor
regressor = DecisionTreeRegressor(criterion = 'mse',
                                  splitter = 'best')
regressor.fit(X, Y)
score = regressor.score(X,Y)

import numpy as np
X_test = np.arange(min(X), max(X), 0.1).reshape(-1,1)
dfXtest = pd.DataFrame(X_test)

import matplotlib.pyplot as plt
plt.scatter(X,Y)
plt.plot(X_test, regressor.predict(X_test), color='red')
plt.title('Regressão com árvores de decisão')   
plt.xlabel('Idade')
plt.ylabel('Custo')

#Uma previsão:
previsao = regressor.predict([[40]])

