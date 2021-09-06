import pandas as pd

#Importação da base
base = pd.read_csv('credit-data.csv')
base.loc[base.age < 0, 'age'] = 40.92
               
#Divisão entre previsores e classe (target)
previsores = base.iloc[:, 1:4].values
classe = base.iloc[:, 4].values

#Préprocessamento dos valores missing
from sklearn.preprocessing import Imputer
imputer = Imputer(missing_values = 'NaN', strategy = 'mean', axis = 0)
imputer = imputer.fit(previsores[:, 1:4])
previsores[:, 1:4] = imputer.transform(previsores[:, 1:4])

#Padronização dos dados
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
previsores = scaler.fit_transform(previsores)

#Divisão dos dados entre teste e treinamento
from sklearn.cross_validation import train_test_split
previsores_treinamento, previsores_teste, classe_treinamento, classe_teste = train_test_split(previsores, classe, test_size=0.25, random_state=0)

#Importação do modelo, instanciamento e treinamento do mesmo
from sklearn.linear_model import LogisticRegression
classifier = LogisticRegression(random_state=1)
classifier.fit(previsores_treinamento, classe_treinamento)

#Visualizar as probabilidades:
probabilidades = classifier.predict_proba(previsores_teste)
#Visualizar os coeficientes:
coeficientes = classifier.coef_
linear_coefficient = classifier.intercept_

#Predição
previsoes = classifier.predict(previsores_teste)

#Ver a acurácia do modelo
from sklearn.metrics import confusion_matrix, accuracy_score
matriz = confusion_matrix(classe_teste, previsoes)
acucaria = accuracy_score(classe_teste, previsoes)

