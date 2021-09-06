setwd("C:\\Users\\Vitor Barbosa\\Google Drive\\DS\\Udemy-R\\S2\\13_Plot")

# Código para limpeza da tela
cat("\014")

#Código para limpar a variable explorer
rm(list=ls())

dados = c(3,4,2,2,1)

# plot(dados)
# plot(dados,type = "l")
#Com linhas transpassando os pontos
plot(dados, type = "o")

#Histograma:
hist(dados)

hist(dados, freq = F)

#barplot
barplot(dados)

#boxplot:
boxplot(dados)

#pizza:
pie(dados)

#Gráfico mais elaborado:
barplot(dados, 
        main = "Título do gráfico",
        xlab = "Nome do eixo x",
        ylab = "Nome do eixo y",
        names.arg= c("Segunda","Terça","Quarta","Quinta","Sexta"))