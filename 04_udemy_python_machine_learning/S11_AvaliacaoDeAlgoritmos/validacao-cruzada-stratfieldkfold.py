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

from sklearn.naive_bayes import GaussianNB

a = np.zeros(5)
previsores.shape
previsores.shape[0]
#Criação de uma matriz de uma coluna de 2000 zeros (Shape samples)
b = np.zeros(shape = (previsores.shape[0],1))

#Importandoo StratifiedKFold
from sklearn.model_selection import StratifiedKFold
from sklearn.metrics import accuracy_score, confusion_matrix

#Pegar diferentes 
kfold = StratifiedKFold(n_splits=10, shuffle=True, random_state=0)
resultados = []
#previsores me retorna n_samples e n_features
#b me retorna n_samples
#Aqui dentro ele vai gerar os índices utilizados em treinamento e teste, os quais são diferentes

for indice_treinamento, indice_teste in kfold.split(previsores, b):
#    print('Índice treinamento:', indice_treinamento, 'Índice teste:', indice_teste )
    classificador = GaussianNB()
    classificador.fit(previsores[indice_treinamento], classe[indice_treinamento]) #fit com os índices de treinamento]
    previsoes = classificador.predict(previsores[indice_teste]) #predict com os índices de teste
    acuracia = accuracy_score(classe[indice_teste], previsoes)
    resultados.append(acuracia)

#Pode-se aqui consultar a última vez que ele gerou os índices
dfindice_treinamento = pd.DataFrame(indice_treinamento)
dfindice_teste = pd.DataFrame(indice_teste)

resultados = np.asanyarray(resultados)    
resultados.mean()
resultados.std()
