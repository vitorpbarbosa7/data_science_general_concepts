#Pacote structure define a estrutura da rede neural
#Rede neural do tipo FeedForwardNetwork
from pybrain.structure import FeedForwardNetwork

#Importando a camada Linear, Sigmoid
from pybrain.structure import LinearLayer, SigmoidLayer, BiasUnit

#Classe que realiza as ligações entre as camadas
from pybrain.structure import FullConnection

#Instanciar o objeto rede neural a partir da Classe Rede Neural
rede = FeedForwardNetwork()

#Instanciando a camada de entrada
#Utilização da LinearLayer porque os valores não serão submetidos 
#à nenhuma função de ativação
CamadaEntrada = LinearLayer(2) #A dimensão (dim) desta camada é 2

#Criação da Camada Oculta
CamadaOculta = SigmoidLayer(3)

#Criação da Camada de Saída
CamadaSaida = SigmoidLayer(1)

#Criação das unidades de bias
#São duas Unidades de Bias, uma para a Oculta e uma para a Saída
bias1 = BiasUnit()
bias2 = BiasUnit()

#Adicinar estas camadas todas dentro da rede neural:
#Do objeto rede, instanciado a partir da classe FeedForwardNetwork
#têm-se o método addModule
rede.addModule(CamadaEntrada)
rede.addModule(CamadaOculta)
rede.addModule(CamadaSaida)
rede.addModule(bias1)
rede.addModule(bias2)

#Uma vez adicinadas todas as Camadas, realizamos a ligação entre elas
LigEntradaOculta = FullConnection(CamadaEntrada, CamadaOculta)
LigOcultaSaida = FullConnection(CamadaOculta, CamadaSaida)
LigBiasOculta = FullConnection(bias1, CamadaOculta)
LigBiasSaida = FullConnection(bias2, CamadaSaida)

#Por fim, vamos chamar o método da rede de construção da rede:
rede.sortModules()

#ALguns print para verificar dados:

#Estrutura da rede
print(rede)

#Parâmetros da ligação entre a camada de Entrada e Oculta
print(LigEntradaOculta.params)

#Parâmetros da ligação entre a camada Oculta e a de Saída
print(LigOcultaSaida.params)
