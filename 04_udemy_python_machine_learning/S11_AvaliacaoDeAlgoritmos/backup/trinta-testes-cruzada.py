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

from sklearn.model_selection import StratifiedKFold
from sklearn.metrics import accuracy_score

#Importação dos diferentes modelos de aprendizagem de máquina
#from sklearn.tree import DecisionTreeClassifier
#from sklearn.naive_bayes import GaussianNB
#from sklearn.ensemble import RandomForestClassifier
#from sklearn.neighbors import KNeighborsClassifier
#from sklearn.linear_model import LogisticRegression
#from sklearn.svm import SVC
#from sklearn.neural_network import MLPClassifier

lista_de_acuracias_30 = []
#for seed in range(30):

kfold = StratifiedKFold(n_splits=10, shuffle=True, random_state = 0)
acuracias = []
for indice_treinamento, indice_teste in kfold.split(previsores, np.zeros(shape=(classe.shape[0], 1))):
#classificador = GaussianNB()
#classificador = DecisionTreeClassifier()
#classificador = RandomForestClassifier(n_estimators=40, criterion='entropy', random_state=0)
#p = 2 significa que utilizará a distância euclidiana
#        classificador = KNeighborsClassifier(n_neighbors=5, metric='minkowski', p=2)
#        classificador = LogisticRegression(random_state=1)
#        classificador = SVC(C=1, kernel='rbf', random_state=1)
#        classificador = MLPClassifier(verbose=True, 
#                                      hidden_layer_sizes=(1000,),
#                                      activation='relu',
#                                      solver = 'adam',
#                                      learning_rate_init=0.001,
#                                      batch_size = 200,
#                                      max_iter = 1000,
#                                      tol=0.00001)
#    classificador.fit(previsores[indice_treinamento], classe[indice_treinamento])
        
#        previsoes = classificador.predict(previsores[indice_teste])
#        acuracia = accuracy_score(classe[indice_teste], previsoes)
#        acuracias.append(acuracia)
#    acuracias = np.asarray(acuracias)
#    media_acuracias = acuracias.mean()
#    lista_de_acuracias_30.append(media_acuracias)
#    
#lista_de_acuracias_30 = np.asarray(lista_de_acuracias_30)    
#lista_de_acuracias_30.mean()

