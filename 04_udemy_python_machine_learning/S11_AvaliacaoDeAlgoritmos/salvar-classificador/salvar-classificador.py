import pandas as pd
import numpy as np
#Gravar arquivos no disco
import pickle

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

#Support Vector Machine
from sklearn.svm import SVC
classificador_svm = SVC(C = 2.0,
                        kernel='rbf',
                        random_state=1,
                        probability=True)

classificador_svm.fit(previsores, classe)
#Para salvar: 
pickle.dump(classificador_svm, open('svm.sav','wb')) 


#Random Forest
from sklearn.ensemble import RandomForestClassifier
classificador_RandomForest = RandomForestClassifier(n_estimators=40,
                                                    criterion='entropy')


classificador_RandomForest.fit(previsores, classe)
#Para salver:
pickle.dump(classificador_RandomForest, open('randomforest.sav', 'wb'))

#Rede neural com Perceptrons
from sklearn.neural_network import MLPClassifier
classificador_MLP = MLPClassifier(max_iter = 1000,
                                  tol = 0.0001,
                                  solver = 'adam',
                                  hidden_layer_sizes=(100),
                                  activation='relu', 
                                  batch_size=200,
                                  learning_rate_init=0.001)

classificador_MLP.fit(previsores, classe)
#Para salvar:
pickle.dump(classificador_MLP, open('MLP.sav', 'wb'))
