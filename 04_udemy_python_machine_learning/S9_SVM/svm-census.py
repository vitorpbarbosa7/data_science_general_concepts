import pandas as pd

base = pd.read_csv('census.csv')

previsores = base.iloc[:, 0:14].values
classe = base.iloc[:, 14].values
                
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
labelencoder_previsores = LabelEncoder()
categorias = [1,3,5,6,7,8,9,13]

for cat in categorias:
    previsores[:,cat] = labelencoder_previsores.fit_transform(previsores[:,cat])

##Aplicação do OneHotEncoder
#onehotencoder = OneHotEncoder()            
#previsores = onehotencoder.fit_transform(previsores, y=None)
    
#Aplicação do OneHotEncoder
onehotencoder = OneHotEncoder(categories=categorias)
previsores = onehotencoder.fit_transform(previsores).toarray()
    
#labelencoder na classe              
labelencoder_classe = LabelEncoder()
classe = labelencoder_classe.fit_transform(classe)

#Antes de aplicar ao modelo o SVM, é necessário normalizar os dados
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
previsores = scaler.fit_transform(previsores)

from sklearn.model_selection import train_test_split
previsores_treinamento, previsores_teste, classe_treinamento, classe_teste = train_test_split(previsores, classe, test_size=0.15, random_state=0)

from sklearn.svm import SVC
classificador = SVC(kernel='rbf', C=1, random_state=1)
classificador.fit(previsores_treinamento, classe_treinamento)
previsoes = classificador.predict(previsores_teste)

from sklearn.metrics import confusion_matrix, accuracy_score
acuracia = accuracy_score(classe_teste, previsoes)
matriz = confusion_matrix(classe_teste, previsoes)

import collections
collections.Counter(classe_teste)