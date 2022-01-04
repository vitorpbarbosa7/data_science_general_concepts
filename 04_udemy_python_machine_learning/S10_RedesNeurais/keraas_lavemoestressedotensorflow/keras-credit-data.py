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

import keras
#Rede neural sequencial, com pesos fluindo da camada de entrada
#Para camada oculta, para a camada de saída
from keras.models import Sequential
#Rede neural do tipo Densa
from keras.layers import Dense
#Criação da rede neural sequencial
classificador = Sequential()
#Criação das camadas
#Cada vez que utilizo o add estou criando uma camada oculta
#Units me dá o número de Neurônios
classificador.add(Dense(units=2,
                  activation = 'relu', #Função rectifier
                  input_dim = 3)) #Número de entradas nesta primeira camada oculta

#Segunda camada
classificador.add(Dense(units=2, activation='relu'))

#Camada de saída:
#Utilizar sigmóide para saídas binárias (Faz sentido)
classificador.add(Dense(units=1, activation='sigmoid'))

#Criação do compilador, onde define-se algortimo de ajuste dos erros
#Algoritmo de cálculo do erro (perda)
#Métrica será pela acurácia
classificador.compile(optimizer='adam',
                      loss='binary_crossentropy',
                      metrics=['accuracy'])

#Realizar o treinamento finalmente
classificador.fit(previsores_treinamento, classe_treinamento,
                  batch_size=10, nb_epoch = 150)

#Treinado o modelo, hora de checar sua previsão 
#Gerou probabilidades
previsoes = classificador.predict(previsores_teste)
previsoes = (previsoes > 0.5) #Onde for 1 vai ser true e isso é equivalente para o algoritmo

from sklearn.metrics import confusion_matrix, accuracy_score
acuracia = accuracy_score(classe_teste, previsoes)
matriz = confusion_matrix(classe_teste, previsoes)
