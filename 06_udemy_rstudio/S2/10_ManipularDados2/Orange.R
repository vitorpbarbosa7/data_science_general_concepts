setwd("C:\\Users\\Vitor Barbosa\\Google Drive\\DS\\Udemy-R\\S2\\10_ManipularDados2")

# Código para limpeza da tela
cat("\014")

#Código para limpar a variable explorer
rm(list=ls())

laranja = Orange

write.csv(laranja, "laranja.csv")

summary(laranja)

x = c(1:3)

#Função dimensão
dim(laranja)
dim(x)

#Função para length
length(x)
#lenght em dataframes mostra o número de colunas
length(laranja) 
#length da coluna me fornece o número de linhas da árvore
length(laranja$Tree) 

#Diretamente o número de linhas:
nrow(laranja)
nrow(x) #Não funciona, vetor não tem linhas
ncol(laranja)
ncol(x) #Não funciona, vetor não tem colunas

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

#Média:
#Coluna não numérica não é possível
#Esta coluna é um fator ordenado
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

