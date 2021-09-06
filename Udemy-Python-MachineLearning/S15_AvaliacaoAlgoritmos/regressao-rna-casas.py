import pandas as pd

base = pd.read_csv('house_prices.csv')

X = base.iloc[:, 3:19].values
y = base.iloc[:, 2:3].values

from sklearn.preprocessing import StandardScaler
scaler_x = StandardScaler()
X = scaler_x.fit_transform(X)
scaler_y = StandardScaler()
y = scaler_y.fit_transform(y)

from sklearn.model_selection import train_test_split
X_treinamento, X_teste, y_treinamento, y_teste = train_test_split(X, y,
                                                                  test_size = 0.3,
                                                                  random_state=0)

from sklearn.neural_network import  MLPRegressor
regressor = MLPRegressor(hidden_layer_sizes=(9,9,),
                         activation='relu',
                         solver='adam',
                         learning_rate_init=0.001,
                         max_iter=1000,
                         random_state=0,
                         tol=1e-6, 
                         verbose=True)

regressor.fit(X_treinamento,y_treinamento)

score_treinamento = regressor.score(X_treinamento, y_treinamento)
score_teste = regressor.score(X_teste, y_teste)

#MAE

from sklearn.metrics import mean_absolute_error
mae = mean_absolute_error(scaler_y.inverse_transform(y_teste),
                          scaler_y.inverse_transform(regressor.predict(X_teste)))
