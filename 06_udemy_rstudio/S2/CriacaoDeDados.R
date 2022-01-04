#Set Working Directory
setwd("C:\\Users\\Vitor Barbosa\\Google Drive\\DS\\Udemy-R\\S2")

#Função rep:

rep("abc", 3)

rep(c("a","b","c"),times = 3)
rep(c("a","b","c"), each = 3)

rep(c("a", "b", "c"), each =3, times = 2)

#Função sample
?sample
sample(1:10,5) #5 valores entre 1 e 10

sample(1:5,10, replace=T)

#Função set.seed para a função sample funcionar de uma maneira pseudo-aleatória
#Como se fosse o random_state no python lindo 
#Assim ele vai gerar sempre o mesmo número
set.seed(22)
sample(1:10,5)

#Criação dos maravilhosos DataFrames:
x = data.frame("a"=1:5, "b" = c("a","b","c","d","e"))

?sample

dados = data.frame("genero" = c(rep("masculino",12),rep("feminino",14)),
                   "altura" = sample(150:172,26,replace = TRUE)/100,
                   "peso" = sample(60:75,26,replace = TRUE),
                   "nota" = sample(4:10,26,replace = TRUE),
                   "lateralidade" = sample(c("canhoto","destro"),26,replace = TRUE, prob =c(0.8,0.2)))

#Sumário das informações do dataframe:
summary(dados)

table(dados)

#Para retornar valor únicos dos dataframes
#Assim que se carrega bibliotecas no R: (No python é mais fofinho import pandas as pd)
library(dplyr)
distinct(dados)

#Dá na mesma essa função built in:
unique.data.frame(dados)

#Para uma coluna:
lateralidade = data.frame(dados$lateralidade)
unique.data.frame(lateralidade)
distinct(lateralidade)

#Carregar outra biblioteca porque estas ai de cima não funcionaram:
library(plyr)
lateralidade_canhoto = sum(ldply(dados$lateralidade, function(c) sum(c=="canhoto")))
#Com certeza há uma maneira mais fácil ainda né

#Salvar os dados com a função write:
write.csv(dados, 'dados1.csv')

#Criando mais colunas:
dados$cor_favorita = c(sample(c("azul","vermelho","verde","amarelo"),26, replace = TRUE))
dados$imc = dados$peso / (dados$altura^2)

View(dados)
head(dados)
