import pickle
from sklearn.preprocessing import StandardScaler
import numpy as np

svm = pickle.load(open('svm.sav', 'rb'))
random_forest = pickle.load(open('randomforest.sav', 'rb'))
mlp = pickle.load(open('mlp.sav', 'rb'))

novo_registro = [[50000, 40, 5000]]
novo_registro = np.asarray(novo_registro)
novo_registro = novo_registro.reshape(-1, 1)
scaler = StandardScaler()
novo_registro = scaler.fit_transform(novo_registro)
novo_registro = novo_registro.reshape(-1, 3)

resposta_svm = svm.predict(novo_registro)
resposta_randomforest = random_forest.predict(novo_registro)
resposta_mlp = mlp.predict(novo_registro)

#Definindo nível de confiança mínima:
confianca_minima = 0.99999999999983

#Qual o nível de confiabilidade dessa previsão?
prob_svm = svm.predict_proba(novo_registro)
confianca_svm = prob_svm.max()

prob_randomforest = svm.predict_proba(novo_registro)
confianca_randomforest = prob_randomforest.max()

prob_mlp = mlp.predict_proba(novo_registro)
confianca_mlp = prob_mlp.max()

paga = 0
nao_paga = 0
if confianca_svm > confianca_minima:
    if resposta_svm[0] == 1:
        paga += 1
    else:
        nao_paga += 1
        
if confianca_randomforest > confianca_minima:
    if resposta_randomforest[0] == 1:
        paga += 1
    else:
        nao_paga += 1
        
if confianca_mlp > confianca_minima:        
    if resposta_mlp[0] == 1:
        paga += 1
    else:
        nao_paga += 1
    
if paga > nao_paga:
    print("O cliente pagará")
else:
    print("O cliente não pagará")
    
paga 
nao_paga

        

