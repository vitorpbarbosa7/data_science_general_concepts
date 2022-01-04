import pandas as pd

#Importação da base
base = pd.read_csv('census.csv')

#Divisão entre previsores e classe
previsores = base.iloc[:, 0:14].values
classe = base.iloc[:, 14].values

#Tratamento utilizado de LabelEnconcer e OneHotEncoder                
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
labelencoder_previsores = LabelEncoder()
vetorlabelencoder = [1,3,5,6,7,8,9,13]
for item in vetorlabelencoder:
    previsores[:,item] = labelencoder_previsores.fit_transform(previsores[:,item])

#Aplicação LabelEncoder
labelencoder_classe = LabelEncoder()
classe = labelencoder_classe.fit_transform(classe)

#Aplicação OneHotEncoder
onehotencoder = OneHotEncoder(categorical_features = [1,3,5,6,7,8,9,13])
previsores = onehotencoder.fit_transform(previsores).toarray()

#Aplicação da Padronização
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
previsores = scaler.fit_transform(previsores)

#Divisão da base em treinamento e teste
from sklearn.cross_validation import train_test_split
previsores_treinamento, previsores_teste, classe_treinamento, classe_teste = train_test_split(previsores, classe, test_size=0.15, random_state=0)

#Importação, instanciamento e aplicação do modelo
from sklearn.linear_model import LogisticRegression
classifier = LogisticRegression(random_state=1)
classifier.fit(previsores_treinamento, classe_treinamento)

#Predição a partir do modelo criado (classificador)
previsoes = classifier.predict(previsores_teste)

#Verificar a acurácia do modelo:
from sklearn.metrics import confusion_matrix, accuracy_score
matriz = confusion_matrix(classe_teste, previsoes)
acuracia = accuracy_score(classe_teste, previsoes)

#Visualização das probabilidades:
proabilidades = classifier.predict_proba(previsores_teste)

#Visualizar coeficientes
coeficientes = classifier.coef_
linear_coef = classifier.intercept_
