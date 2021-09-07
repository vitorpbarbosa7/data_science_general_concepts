setwd("C:\\Users\\Vitor Barbosa\\Google Drive\\DS\\Udemy-R\\S2\\15_Valores_Missing")

# Código para limpeza da tela
cat("\014")

#Código para limpar a variable explorer
rm(list=ls())

#Dataframe para lidar com valores missing
dados = data.frame("a"=c(1,3,NA), "b" = c(4,NA,4), "c" = c(3,3,3))

#Escrever esse banco de dados em csv para checar como isso acontece no pandas:
write.csv(dados, 'dados.csv')
dados
 
mean(dados$c)
#Não é possível executar a média de uma coluna com valores faltantes
mean(dados$a)

mean(dados$a, na.rm = T)

#Já desconsidera o valor Missing no Summary
summary(dados)

#Função na.omit:Retorna as linhas que não contém valores missing
?na.omit()

na.omit(dados)
dados

#na.fail apenas retorna o objeto se ele não contém Missing Values
na.fail(dados)

#complete.cases: retorna quais linhas possuem todos valores e os quais não possuem 
complete.cases(dados)

#Treinando acessar os valores no data.frame:
dados[3,3]
dados[,]

#Retorna todas as colunas das linhas com o valor lógico TRUE
dados[complete.cases(dados),] 

class(complete.cases(dados))
length(complete.cases(dados))

#Avaliação de na em todos elementos:
is.na(dados)

#Substituição:
dados[is.na(dados)==TRUE] = 0
dados
