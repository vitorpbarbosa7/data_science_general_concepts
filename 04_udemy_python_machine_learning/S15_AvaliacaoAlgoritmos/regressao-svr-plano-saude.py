import pandas as pd

base = pd.read_csv('plano_saude2.csv')

X = base.iloc[:, 0:1].values
y = base.iloc[:, 1:2].values

#Escalonamento para utilizar SUPPORT VECTOR MACHINE
from sklearn.preprocessing import StandardScaler
scaler_x = StandardScaler()
scaler_y = StandardScaler()
X = scaler_x.fit_transform(X)
y = scaler_y.fit_transform(y.reshape(-1,1))

#Teste com kernel linear:
from sklearn.svm import SVR
regressor_linear = SVR(kernel = 'linear',
                       epsilon=0.1)

regressor_linear.fit(X,y)

import matplotlib.pyplot as plt
plt.scatter(X, y)
plt.plot(X, regressor_linear.predict(X), color = 'red')

score_linear = regressor_linear.score(X, y)

#Regressor polinomial com vetores de suporte:
regressor_poly = SVR(kernel='poly',
                     degree=3)
regressor_poly.fit(X,y)

score_poly = regressor_poly.score(X,y)

plt.scatter(X, y)
plt.plot(X, regressor_poly.predict(X), color = 'red')

#Regressor com rbf (Radial Basis Function)
regressor_rbf = SVR(kernel='rbf',
                    epsilon=0.1)

regressor_rbf.fit(X,y)

score_rbf = regressor_rbf.score(X,y)

plt.scatter(X, y)
plt.plot(X, regressor_rbf.predict(X), color = 'red')

#Dado que anteriormente tinhamos realizado a padronização dos dados, agora é preciso realizar a transformação inversa
previsao_linear = scaler_y.inverse_transform(regressor_linear.predict([[40]]))
previsao_poly = scaler_y.inverse_transform(regressor_poly.predict([[40]]))
previsao_svm = scaler_y.inverse_transform(regressor_rbf.predict([[40]]))
