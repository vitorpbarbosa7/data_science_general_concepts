setwd("C:\\Users\\Vitor Barbosa\\Google Drive\\DS\\Udemy-R\\S2\\10_ManipularDados2")

# C�digo para limpeza da tela
cat("\014")

#C�digo para limpar a variable explorer
rm(list=ls())

laranja = Orange

write.csv(laranja, "laranja.csv")

summary(laranja)

x = c(1:3)

#Fun��o dimens�o
dim(laranja)
dim(x)

#Fun��o para length
length(x)
#lenght em dataframes mostra o n�mero de colunas
length(laranja) 
#length da coluna me fornece o n�mero de linhas da �rvore
length(laranja$Tree) 

#Diretamente o n�mero de linhas:
nrow(laranja)
nrow(x) #N�o funciona, vetor n�o tem linhas
ncol(laranja)
ncol(x) #N�o funciona, vetor n�o tem colunas

#Nome das linhas
rownames(laranja)

#Nome das colunas
colnames(laranja)

names(laranja)

#Atribuindo nomes aos valores do vetor:
?names
names(x) = c("a","b","c")

x

#Trabalhando com formato de dados
#Retornando formato dos dados:
class(x)

class(laranja)
class(laranja$Tree)
class(laranja$age)
class(laranja$circumference)

#M�dia:
#Coluna n�o num�rica n�o � poss�vel
#Esta coluna � um fator ordenado
mean(laranja$Tree) 
mean(laranja$circumference)
mean(laranja$age)

a = colMeans(data.frame(laranja$age,laranja$circumference))

#Transformar em caracter:
laranja$Tree = as.character(laranja$Tree)

#Para converter para outros formatos, temos:

as.factor() 
as.character()
as.numeric()
as.integer()

