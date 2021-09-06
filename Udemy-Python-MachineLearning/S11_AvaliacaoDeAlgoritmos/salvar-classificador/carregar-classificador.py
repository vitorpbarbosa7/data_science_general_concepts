import pandas as pd
import pickle
from sklearn.preprocessing import StandardScaler
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

scaler = StandardScaler()
previsores = scaler.fit_transform(previsores)

svm = pickle.load(open('svm.sav', 'rb'))
random_forest = pickle.load(open('randomforest.sav', 'rb'))
mlp = pickle.load(open('MLP.sav', 'rb'))

acuracia_svm = svm.score(previsores, classe)
acuracia_randomforest = random_forest.score(previsores, classe)
acuracia_mlp = mlp.score(previsores, classe)

novo_registro = np.asanyarray([[50000, 40, 5000]])
#Reshape para depois aplicar escalonamento
novo_registro = novo_registro.reshape(-1,1)
#Escolonamento por coluna (por isso foi necessário o reshape)
novo_registro = scaler.fit_transform(novo_registro)
#Voltando para o formato de linha:
#-1 Não mexa nas linhas. #Mas quero 3 colunas
novo_registro = novo_registro.reshape(1,3)

#No svm:
resposta_svm = svm.predict(novo_registro)

#Resposta RandomForest
resposta_randomforest = random_forest.predict(novo_registro)

#Resposta MLP:
resposta_mlp = mlp.predict(novo_registro)
