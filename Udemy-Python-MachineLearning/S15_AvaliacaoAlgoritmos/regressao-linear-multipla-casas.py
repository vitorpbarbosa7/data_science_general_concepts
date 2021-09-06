import pandas as pd

base = pd.read_csv('house_prices.csv')

X = base.iloc[:, 3:19].values
Y = base.iloc[:, 2].values

from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, 
                                                    test_size = 0.3,
                                                    random_state = 0)

correlacao = base.corr()

from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train, Y_train)

#Coeficiente de determinação com dados de treinamento
regressor.score(X_train, Y_train)
#Coeficiente de determinação com dados de teste
regressor.score(X_test, Y_test)

coeficientes = regressor.coef_

#Realizando as predições:
previsoes = regressor.predict(X_test)

from sklearn.metrics import mean_absolute_error, mean_squared_error
mae = mean_absolute_error(Y_test, previsoes)
msq = mean_squared_error(Y_test, previsoes)