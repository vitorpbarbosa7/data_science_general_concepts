import pandas as pd
import numpy as np

base = pd.read_csv('plano_saude2.csv')

X = base.iloc[:, 0:1].values
y = base.iloc[:, 1:2].values

#Escalonamento:
from sklearn.preprocessing import StandardScaler
scaler_X = StandardScaler()
X = scaler_X.fit_transform(X)
scaler_y = StandardScaler()
y = scaler_y.fit_transform(y)

#Neural Network 
from sklearn.neural_network import MLPRegressor
regressor = MLPRegressor(hidden_layer_sizes=(100,100,),
                         activation='relu', 
                         solver='adam',
                         learning_rate_init=0.0001,
                         verbose=True,
                         max_iter = 1000,
                         tol=0.000001,
                         random_state=0)

regressor.fit(X,y)
score = regressor.score(X,y)

import matplotlib.pyplot as plt
plt.scatter(scaler_X.inverse_transform(X), 
            scaler_y.inverse_transform(y))

plt.plot(scaler_X.inverse_transform(X), 
         scaler_y.inverse_transform(regressor.predict(X)),
         color = 'red')

plt.title('Regressão com redes neurais')
plt.xlabel('Idade')
plt.ylabel('Custo')