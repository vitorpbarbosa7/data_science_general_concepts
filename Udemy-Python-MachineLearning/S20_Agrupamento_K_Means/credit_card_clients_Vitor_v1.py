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
X = base.iloc[:,[1,25]]
#Padrão do numpy exige .values
XX = base.iloc[:,[1,25]].values

#Escalonamento:
scaler = StandardScaler()
X = scaler.fit_transform(X)

#Otimização do número de clusters escolhido de acordo com o Elbow Method:
wcss = []
for i in range(1,11):
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
plt.scatter(X[:,0],X[:,1], c=previsoes)
plt.xlabel('Limite do cartão de crédito')
plt.ylabel('Soma total das últimas faturas')

#Outra maneira de plotar:
cores = ['red','orange','green','blue']
rotulos = ['C1','C2','C3','C4']
for i in range(0,4):
    plt.scatter(X[previsoes == i, 0], X[previsoes ==i, 1],  c = cores[i], label = rotulos[i])
plt.xlabel('Limite do cartão de crédito')
plt.ylabel('Soma total das últimas faturas')
plt.legend()

#Visualizar os clientes:
#column_stack permite juntar duas bases com equivalencia das linhas
lista_clientes = np.column_stack((base, previsoes))

#Agora para realizar a ordenação:
ordenamento = pd.DataFrame(lista_clientes[:,26].argsort()
lista_clientes = lista_clientes[lista_clientes[:,26].argsort()]
