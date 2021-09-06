import pandas as pd

base = pd.read_csv('house_prices.csv')

X = base.iloc[:, 3:19].values
y = base.iloc[:, 2:3].values

X[[3][:]]

#Primeiramente o escalonamento 
from sklearn.preprocessing import StandardScaler
scaler_X = StandardScaler()
X = scaler_X.fit_transform(X)

#Observa-se que o scaler_x consegue voltar o escalonamento, o que é lindo
X[[3][:]]
scaler_X.inverse_transform(X[[3][:]])

scaler_y = StandardScaler()
y = scaler_y.fit_transform(y)

from sklearn.model_selection import train_test_split
X_treinamento, X_teste, y_treinamento, y_teste = train_test_split(X, y,
                                                                  test_size = 0.3,
                                                                  random_state = 0)

from sklearn.svm import SVR
regressor = SVR(C =5,
                kernel='rbf', epsilon=0.1,
                degree=3)

regressor.fit(X_treinamento,y_treinamento)

score_treinamento = regressor.score(X_treinamento, y_treinamento)
score_teste = regressor.score(X_teste, y_teste)

from sklearn.metrics import mean_absolute_error

mae = mean_absolute_error(scaler_y.inverse_transform(y_teste), 
                          scaler_y.inverse_transform(regressor.predict(X_teste)))

#Previsão. Deve-se aplicar inverse_traansform porque foi realizado o escalonamento
previsao1 = scaler_y.inverse_transform(regressor.predict(X[[3][:]]))
