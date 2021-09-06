import pandas as pd

base = pd.read_csv('house_prices.csv')

X = base.iloc[:, 3:19].values
Y = base.iloc[:, 2].values

from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, 
                                                    test_size=0.3,
                                                    random_state = 0)

from sklearn.preprocessing import PolynomialFeatures
poly = PolynomialFeatures(degree = 4)
#Após fit_transform, pode usar só transform, mas não entendi porque não. 
X_train_poly = poly.fit_transform(X_train)
X_test_poly = poly.transform(X_test)

from sklearn.linear_model import LinearRegression
regressor1 = LinearRegression()
regressor1.fit(X_train_poly, Y_train)

#Scores:
score_treinamento = regressor1.score(X_train_poly, Y_train)
score_teste = regressor1.score(X_test_poly, Y_test)

previsoes = regressor1.predict(X_test_poly)

from sklearn.metrics import mean_absolute_error
mae = mean_absolute_error(Y_test, previsoes)
