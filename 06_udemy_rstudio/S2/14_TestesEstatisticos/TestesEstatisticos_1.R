setwd("C:\\Users\\Vitor Barbosa\\Google Drive\\DS\\Udemy-R\\S2\\14_TestesEstatisticos")

# Código para limpeza da tela
cat("\014")

#Código para limpar a variable explorer
rm(list=ls())
# 
# ?data
# data()

dados = read.csv("Flowrates_.csv",skip = 1,sep = ";")
dados = data.frame(dados)

#Renomeando a primeira coluna:
names(dados)[1] = "tempo"
#Coeficiente de correlação:
cor(dados$x2,dados$x3)

#Matriz de correlação 
cor(dados[,2:ncol(dados)])

#Teste de correlação:
cor.test(dados$x2,dados$x3)

dados$x6 = sample(1:10,length(dados), replace = TRUE)
#Teste t:
t.test(dados$x2,dados$x6)

#Teste t:
?t.test

t.test()

#Brincando com o dataset Orange mesmo:
laranja = Orange

#Teste de hipótese da diferença entre as médias
#Separar qual é meu banco de dados
laranja2=Orange[Orange$Tree=="1"|Orange$Tree=="2",]
#Comparar média das circunferências com as idades das laranjas não é mio estranho?
t.test(laranja2$circumference~laranja2$Tree)
