import pandas as pd 

base = pd.read_csv('credit-data.csv')
base = base.dropna()

#Outliers baseado em distâncias:
from pyod.models.knn import KNN
detector = KNN()
#Treinamento do detector de outliers por knn
detector.fit(base.iloc[:,1:4])

#Baseado nas distâncias, diz se é ou não é outlier
previsoes = detector.labels_
confianca_previsoes = detector.decision_scores_

detector_df = pd.DataFrame(previsoes, confianca_previsoes)
detector_df = detector_df.reset_index()
detector_df.columns = [ 'Confianca','Boleano']

detector_df = detector_df[['Boleano', 'Confianca']]

detector_df = detector_df.sort_values(by='Boleano', ascending=False)

import matplotlib.pyplot as plt



#Lista de outliers:
outliers = []
for i in range(len(previsoes)):
    if previsoes[i] ==1:
        outliers.append(i)
        

#Como retornar todas linhas de outliers
lista_outliers = base.iloc[outliers, :]
