import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt

base = pd.read_csv('plano-saude.csv')

#Separar previsores de dependentes:
#Values transforma para numpy array
X = base.iloc[:,0].values
Y = base.iloc[:,1].values

#Há correlaação entre estas variáveis:
corr = base.corr()

correlacao = np.corrcoef(X, Y)

#Reshape para transformar em matriz:
#Algoritmos do scikit learn precisam trabalhar com matrizes
#Não mexe nas linhas e adiciona uma coluna (a própria coluna)
X = X.reshape(-1,1)

#Modelo linear de regressão:
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X, Y)

#Acurácia:
regressor.score(X, Y)

#Predição:
regressor.predict([[50]])

figura1 = plt.figure(figsize=(5,5), dpi=150)
plt.scatter(X, Y)
plt.plot(X, regressor.predict(X), '--')
plt.title('Regressão linear simples')
plt.xlabel('Idade (anos)')
plt.ylabel('Custo do plano de saúde (R$)')
figura1.show()
#plt.scatter(50, regressor.predict([[50]]), 'o')

angular = regressor.coef_
interseccao = regressor.intercept_

residuo = regressor._residues

#Yellow Brick
figura2 = plt.figure(figsize = (3,3), dpi=150)
from yellowbrick.regressor import ResidualsPlot
visualizador = ResidualsPlot(regressor)
visualizador.fit(X,Y)
#visualizador.score(X, Y)
visualizador.show()
figura2.show()