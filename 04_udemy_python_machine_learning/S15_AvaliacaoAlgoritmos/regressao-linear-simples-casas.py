import pandas as pd
import matplotlib.pyplot as plt


base = pd.read_csv('house_prices.csv')

#Metragem quadrada
#Neste formato [:,5:6] ele já retorna uma matriz
X = base.iloc[:,5:6].values
Y = base.iloc[:,2].values

#plt.scatter(base.sqft_living, base.price)
#plt.show()

#Treinamento e teste:
from sklearn.model_selection import train_test_split
#Random_state= 0 garante sempre a mesma divisão na base de dados
X_train, X_test, Y_train, Y_test = train_test_split(X, Y,
                                                    test_size = 0.3,
                                                    random_state = 0)

#realizar o treinamento:
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train, Y_train) 

acuracia_teste = regressor.score()


figura1 = plt.figure(figsize = (3,3), dpi=150)
plt.scatter(X_train, Y_train)
plt.plot(X_train, regressor.predict(X_train), color = 'red')
plt.title('Regressão linear simples')
plt.xlabel('Pés quadrados da sala')
plt.ylabel('Preço da casa')
figura1.show()

from sklearn.metrics import mean_absolute_error, mean_squared_error
mae = mean_absolute_error(X_test, regressor.predict(X_test))
mse = mean_squared_error(X_test, regressor.predict(X_test))

#Yellow Brick
figura2 = plt.figure(figsize = (3,3), dpi = 150)
from yellowbrick.regressor import ResidualsPlot
visualizador = ResidualsPlot(regressor)
visualizador.fit(X_train, Y_train)
visualizador.score(X_test, Y_test)
visualizador.show()
figura2.show()

#Base de testee:
figura1 = plt.figure(figsize = (3,3), dpi=150)
plt.scatter(X_test, Y_test)
plt.plot(X_test, regressor.predict(X_test), color = 'red')
plt.title('Regressão linear simples')
plt.xlabel('Pés quadrados da sala')
plt.ylabel('Preço da casa')
figura1.show()

