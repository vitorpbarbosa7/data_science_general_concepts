import pickle
from sklearn.preprocessing import StandardScaler
import numpy as np

svm = pickle.load(open('svm.sav', 'rb'))
random_forest = pickle.load(open('randomforest.sav', 'rb'))
mlp = pickle.load(open('MLP.sav', 'rb'))

#O idiota criou como lista primeiro, ai num dá né
novo_registro = [[50000, 40, 5000]]
#Então como vetor
novo_registro = np.asanyarray(novo_registro)
#Depois como 3 linhas e 1 coluna
novo_registro =  novo_registro.reshape(-1,1)

#Escalonar o novo registro. Óia como dá trabalho
scaler = StandardScaler()
novo_registro = scaler.fit_transform(novo_registro)
novo_registro =  novo_registro.reshape(-1,3)

resposta_svm = svm.predict(novo_registro)
resposta_randomforest = random_forest.predict(novo_registro)
resposta_mlp = mlp.predict(novo_registro)


#Utilizando a resposta de 3 algoritmos diferentes
#Inicializando as variávies de pagamento ou não pagamento
paga = 0
nao_paga = 0

if resposta_svm[0] == 1:
    paga += 1
else:
    nao_paga += 1
    
if resposta_randomforest[0] == 1:
    paga += 1
else:
    nao_paga += 1
    
if resposta_mlp[0] == 1:
    paga += 1
else:
    nao_paga += 1
    
if paga > nao_paga:
    print("O cliente pagará")
else:
    print("O cliente não pagará")
        