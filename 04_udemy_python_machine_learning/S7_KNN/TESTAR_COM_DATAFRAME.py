import pandas as pd

base = pd.read_csv('census.csv')

from sklearn.preprocessing import LabelEncoder, OneHotEncoder

labelencoder_classe = LabelEncoder()
classe = labelencoder_classe.fit_transform(base.income)

from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
previsores = scaler.fit_transform(previsores)

from sklearn.cross_validation import train_test_split
previsores_treinamento, previsores_teste, classe_treinamento, classe_teste = train_test_split(previsores, classe, test_size=0.15, random_state=0)

#"Modelo" que na realidade não é um modelo porque o KNN não gera modelo 
from sklearn.neighbors import KNeighborsClassifier
classificador = KNeighborsClassifier(n_neighbors=10,metric='minkowski', p=2)
classificador.fit(previsores_treinamento, classe_treinamento)
previsoes = classificador.predict(previsores_teste)

from sklearn.metrics import accuracy_score, confusion_matrix
acuracaria = accuracy_score(classe_teste, previsoes)
matriz = confusion_matrix(classe_teste, previsoes)

import collections
collections.Counter(classe_teste)