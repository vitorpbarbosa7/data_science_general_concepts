import pandas as pd
import numpy as np

base = pd.read_csv('credit-data.csv')
base.loc[base.age < 0, 'age'] = 40.92
               
previsores = base.iloc[:, 1:4].values
classe = base.iloc[:, 4].values

#Importar o Imputer para tratar valores missing
from sklearn.impute import SimpleImputer
#Instanciar o objeto a partir da classe importada e passar os
#Parâmetros de como tratar os valores missing
imputer = SimpleImputer(missing_values=np.nan, strategy='mean')
#Rodar o imputer
imputer.fit(previsores[:,1:4])
#Vamos Padronizar os dados
previsores[:,1:4] = imputer.fit_transform(previsores[:,1:4])

from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
previsores = scaler.fit_transform(previsores)

from sklearn.model_selection import train_test_split
previsores_treinamento, previsores_teste, classe_treinamento, classe_teste = train_test_split(previsores, classe, test_size=0.25, random_state=0)

#100 neurônios na camada oculta. Precisa de tudo isso?
from sklearn.neural_network import MLPClassifier
classificador = MLPClassifier(verbose = True,
                              max_iter=1000,
                              tol=0.00001,
                              solver='adam',
                              hidden_layer_sizes=(10,),
                              activation='relu',
                              learning_rate_init=0.001,
                              momentum=0.9)

classificador.fit(previsores_treinamento, classe_treinamento)

previsoes = classificador.predict(previsores_teste)

from sklearn.metrics import confusion_matrix, accuracy_score
acuracia = accuracy_score(classe_teste, previsoes)
matriz = confusion_matrix(classe_teste, previsoes)
