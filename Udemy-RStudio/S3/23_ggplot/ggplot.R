setwd("C:\\Users\\Vitor Barbosa\\Google Drive\\DS\\Udemy-R\\S3\\19_barplot")

# CÃ³digo para limpeza da tela
cat("\014")

#CÃ³digo para limpar a variable explorer
rm(list=ls())

library(ggplot2)

laranja = Orange
porco = ToothGrowth
names(laranja)
#Histograma
qplot(x = circumference, data=laranja)

qplot(x = circumference, data=laranja,
      geom = "histogram",
      binwidth = 10)

#Densidade:
qplot(x = circumference, data=laranja,
      geom = "density")

qplot(x = dose, data=porco,
      geom = 'bar')

qplot(x=age, y=circumference, data=laranja)

qplot(x=age, y=circumference, data=laranja,
      geom = "path")

#Color (Hue in python) - Como colorir de acordo com a legenda
qplot(x=age, y=circumference, data=laranja,
      color=Tree)

#Mudança de tamanho das bolinhas
#Mudança de formato 
#Mudança de cor
qplot(supp, dose, data = porco, size=len, color = dose,
      shape = supp)

#Carnaval de configurações para o dataframe laranja:
library(RColorBrewer)
names(laranja)
qplot(x = Tree, y=circumference, data = laranja,
      size = circumference, 
      color = Tree,
      shape = Tree)

