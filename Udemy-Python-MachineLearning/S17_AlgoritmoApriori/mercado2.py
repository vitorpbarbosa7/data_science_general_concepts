import pandas as pd

dados = pd.read_csv('mercado2.csv', header = None)
transacoes = []

for i in range(0, 7501):
    transacoes.append([str(dados.values[i,j]) for j in range(0,20)])

#Vendas de um produto 4 vezes por dia (média), logo na semana serão 7 x 4 vendas na semana
suporte_minimo = 4*7/dados.shape[0]

from apyori import apriori
regras = apriori(transacoes,
                 min_support=suporte_minimo,
                 min_confidence = 0.5, 
                 min_lift = 3.0, 
                 min_length = 2)

resultados = list(regras)

resultados2 = [list(x) for x in resultados]

resultadoFormatado = []

for j in range(0,5):
    resultadoFormatado.append([list(x) for x in resultados2[j][2]])
resultadoFormatado
