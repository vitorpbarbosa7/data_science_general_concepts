require(TStools)
dados = read.csv('D:/Drive_USP/DS/Udemy/S11/Testes_estatisticos_preenchido/dados-testes.csv')
  #Transformar em matriz estes dados
matriz = as.matrix(dados)
TStools::nemenyi(matriz, conf.int = 0.95, plottype = "vline")
#Esta função agora está em tsutils e não em TStools
tsutils::nemenyi(matriz, conf.int = 0.95, plottype = "vline")
#Não houve diferença estatística entre RandomForest e as redes neurais
          