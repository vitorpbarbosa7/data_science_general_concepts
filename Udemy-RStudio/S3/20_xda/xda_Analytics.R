setwd("C:\\Users\\Vitor Barbosa\\Google Drive\\DS\\Udemy-R\\S3\\19_barplot")

# CÃ³digo para limpeza da tela
cat("\014")

#CÃ³digo para limpar a variable explorer
rm(list=ls())

iris = iris

#Biblioteca com ferramentas de desenvolvedores
library(devtools)

#Uma vez carregado o devtools, posso utilizar a função install_github
install_github("ujjwalkarn/xda")

#Agora carregar o pacote Exploratory Data Analysis
library(xda)

#Sumário das informações do dataset
numSummary(iris)

#Resumo das variáveis categóricas
charSummary(iris)

#Dados bivariados:
bivariate(iris, "Sepal.Length", "Sepal.Width")

bivariate(iris, "Species", "Sepal.Length")

#plots:
Plot(iris,"Petal.Length")
Plot(iris,"Petal.Width")
Plot(iris,"Sepal.Width")
Plot(iris,"Sepal.Length")
