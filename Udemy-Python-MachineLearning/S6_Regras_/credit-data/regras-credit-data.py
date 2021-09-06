import Orange

base = Orange.data.Table("credit-data.csv")
#Mostrando o título das features?
base.domain

#Split dos dados em treino e teste
base_dividida = Orange.evaluation.testing.sample(base, 0.25)

#Separando em dois, treinamento e teste a partir de base_dividida
base_treinamento  = base_dividida[1]
base_teste = base_dividida[0]
#Tamanho dos vetores/listas/seilaquetipoehesse
len(base_teste)
len(base_treinamento)

##Treinamento do modelo:
#Primeiramento instanciar um objeto que possa aprender 
cn2_learner = Orange.classification.rules.CN2Learner()
#Agora fazer o objeto aprender
classificador = cn2_learner(base_treinamento)

#Visualizar as regras
for regras in classificador.rule_list:
    print(regras)
    
#Testar o método
resultado = Orange.evaluation.testing.TestOnTestData(base_treinamento, base_teste, [classificador])

#Visualizar a acurária:
print(Orange.evaluation.CA(resultado))