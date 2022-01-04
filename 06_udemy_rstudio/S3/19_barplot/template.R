setwd("C:\\Users\\Vitor Barbosa\\Google Drive\\DS\\Udemy-R\\S3\\19_barplot")

# CÃ³digo para limpeza da tela
cat("\014")

#CÃ³digo para limpar a variable explorer
rm(list=ls())

dados = 4:8

names(dados)
names(dados) = 1:5
dados
names(dados) = c("a","b","c","d","e")
names(dados) = c("abacate","beringela","cebola","laranja","pera")

#Biblioteca de cores:
library(RColorBrewer)
?brewer.pal
cores = brewer.pal(5, "Paired")
# 
# Accent	8
# Dark2	8
# Paired	12
# Pastel1	9
# Pastel2	8
# Set1	9
# Set2	8
# Set3	12

barplot(dados,
        xlab = "Elementos",
        ylab = "Quantidades",
        col = cores,
        border = cores)


#Orange
laranja = Orange
porco = ToothGrowth

?ToothGrowth

dim(table(porco$supp))

#barplot por suplemento
barplot(tapply(porco$len, porco$supp, mean),
        xlab = "Suplemento",
        ylab = "Média do comprimento do dente",
        col = brewer.pal(dim(table(porco$supp)),"Pastel1"))

example("barplot")
?barplot
#barplot por dose:
barplot(tapply(porco$len, porco$dose, mean),
        xlab = "Dose",
        ylab = "Média do comprimento do dente",
        col = brewer.pal(dim(table(porco$dose)),"Pastel1"))

#Base orange
barplot(tapply(laranja$circumference,laranja$age, mean),
        xlab = "Idade da laranjeira",
        ylab = "Circunferência da laranja",
        col = brewer.pal(dim(table(laranja$age)),"Pastel1"),
        main = "Circuferência da laranja em função da idade",
        la)

    