import matplotlib.pyplot as plt
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import numpy as np

base = pd.read_csv('credit_card_clients.csv', header=1)

#Criação do atributo com a soma de todaas faturas:
base['BILL_TOTAL'] = base.iloc[:,12:18].sum(axis=1)

#Realizar o processo de clusterização de 2 em 2 atributos
#Selecionar quais atributos eu quero 
X = base.iloc[:,[1,2,3,4,5,25]]
#Padrão do numpy exige .values
#XX = base.iloc[:,[1,25]].values

#Escalonamento:
scaler = StandardScaler()
X = scaler.fit_transform(X)

#Otimização do número de clusters escolhido de acordo com o Elbow Method:
wcss = []
for i in range(1,30):
    kmeans = KMeans(n_clusters=i,
                    random_state=0)
    kmeans.fit(X)
    wcss.append(kmeans.inertia_)
    
plt.plot(wcss)

#Agora que foi decidido quantos clusters devemos utilizar:
kmeans = KMeans(n_clusters=4,
                init = 'k-means++',
                n_init=10,
                random_state=0,
                verbose=0)

#De acordo com o total de crédito fornecido e a soma de todas faturas dos últims 6 meses a distribuição de clusters será:
#Função fit_predict permite realizar o fit juntamente à já realizar as previsões]

previsoes = kmeans.fit_predict(X)
previsoes_df = pd.DataFrame(previsoes)

#Visualizar os clientes:
#column_stack permite juntar duas bases com equivalencia das linhas
lista_clientes = np.column_stack((base, previsoes))

#Agora para realizar a ordenação:
ordenamento = pd.DataFrame(lista_clientes[:,26].argsort()) #Retorna a ordenação de cada
lista_clientes = pd.DataFrame(lista_clientes[lista_clientes[:,26].argsort()])
