import pandas as pd

base = pd.read_csv('house_prices.csv')

X = base.iloc[:, 3:19].values
Y = base.iloc[:, 2].values

from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(X, Y,
                                                    test_size = 0.3,
                                                    random_state = 0)

from sklearn.tree import DecisionTreeRegressor
regressor = DecisionTreeRegressor(criterion='mse',
                                  splitter='best')

regressor.fit(X_train, Y_train)
acuracia_treinamento = regressor.score(X_train, Y_train)
acuracia_teste = regressor.score(X_test, Y_test)

previsoes = regressor.predict(X_test)

#Olhar o MEAN ABSOLUTE ERROR e o COEFICIENTE DE DETERMINAÇÃO 
#NA BASE DE TESTE

from sklearn.metrics import mean_absolute_error
mae = mean_absolute_error(Y_test, previsoes)


