import pandas as pd 

base = pd.read_csv('risco-credito2.csv')
#Separação entre previsores e classe:
previsores = base.iloc[:,0:4].values
classe = base.iloc[:,4].values

#Aplicação do LabelEnconder
from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
#Aplicar para todos previsores e não para a classe
for i in range(4):
    previsores[:,i] = le.fit_transform(previsores[:,i])
    
#Modelos lineares, para importar a logisticregression
from sklearn.linear_model import LogisticRegression
classifier = LogisticRegression()
classifier.fit(previsores, classe)
#Fazendo uma previsão simples comparando com o do caderno:
resultado1 = classifier.predict([[0,0,1,2]])
#Printando
resultado

#Visualizar a probabilidade
resultado2 = classifier.predict_proba([[0,0,1,2]])
resultado2

#Retornando coeficientes e intercecção
print(classifier.intercept_)
print(classifier.coef_)

