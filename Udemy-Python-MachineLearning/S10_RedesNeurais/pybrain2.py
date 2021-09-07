#Para não fazer a construção manual, vamos utilizar os atalhos
#Construir a rede
from pybrain.tools.shortcuts import buildNetwork
#Banco de dados supervisionado
from pybrain.datasets import SupervisedDataSet
#Treinamento dos pesos realizado com o Backpropagation
from pybrain.supervised.trainers import BackpropTrainer
#Importação da camada com a função de ativação Softmax
from pybrain.structure.modules import SoftmaxLayer
#Importação de uma camada com função de ativação Sigmoid
from pybrain.structure.modules import SigmoidLayer

#Criação da rede neural
#rede = buildNetwork(2, 3, 1)
#rede = buildNetwork(2,3,1, outclass = SoftmaxLayer, 
#                    hiddenclass = SigmoidLayer, bias = False)
# #Por padrão a camada de entrada possui função de ativação do tipo Linear Layer (Não sofre nenhuma transforçamação)
print(rede['in'])
#Default da camada oculta é a função sigmoid
print(rede['hidden0'])
#Linear Layer na camada de saída por Default
print(rede['out'])
#Por padrão ele utiliza sim um Bias
print(rede['bias'])

#Mais uma vez a rede
rede = buildNetwork(2,3,1)
#Definição da base de dados
#Neste caso 2 previsores e 1 classe
base = SupervisedDataSet(2,1)

#Adição dos elementos: (Tabela XOR)
base.addSample((0,0), (0, ))
base.addSample((0,1), (1, ))
base.addSample((1,0), (1, ))
base.addSample((1,1), (0, ))

#Visualizar a base:
print(base['input'])
print(base['target'])

#Instanciamento do objeto treinamento que efetivamente será treinado
#nas épocas de treinamento da rede neural
treinamento = BackpropTrainer(rede, dataset = base, learningrate = 0.01,
                              momentum = 0.06)

#Épocas de treinamento: (Número de vezes que apresento dados para treinamento)
for i in range(1, 30000):
    erro = treinamento.train()
    if i%1000 == 0:
        print("Erro: %s" % erro)
    
#Retornando a resposta:
print(rede.activate([0,0]))
print(rede.activate([0,1]))
print(rede.activate([1,0]))
print(rede.activate([1,1]))