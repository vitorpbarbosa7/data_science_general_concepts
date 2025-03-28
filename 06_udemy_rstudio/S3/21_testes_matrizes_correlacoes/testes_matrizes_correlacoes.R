setwd("C:\\Users\\Vitor Barbosa\\Google Drive\\DS\\Udemy-R\\S3\\21_testes_matrizes_correlacoes")

# Código para limpeza da tela
cat("\014")

#Código para limpar a variable explorer
rm(list=ls())

#Buscar dados
data()
#Carregando o dataset sem a necessidade de atribuir a uma vari�vel:
data("Orange")

View(Orange)

#Plot:
plot(Orange$age,Orange$circumference,
     ylab = "Circumfer�ncia",
     xlab = "Idade da �rvore")

#Apenas correla��o
cor(Orange$age,Orange$circumference)

#Teste de correla��o
cor.test(Orange$age,Orange$circumference)

#Outros tipos de correla��o:
cor.test(Orange$age,Orange$circumference,
         method="pearson")

cor.test(Orange$age,Orange$circumference,
         method="kendall")

cor.test(Orange$age,Orange$circumference,
         method="spearman")


#Utiliza��o das matrizes de correla��o:
data(mtcars)

carros = mtcars

library(corrplot)

correlacao = cor(carros)
corrplot(correlacao, 
         method = 'number',
         type = 'upper')

#Pacote Hmisc (Harrell Miscellaneous)
install.packages("Hmisc")
library(Hmisc)
corr2 = rcorr(as.matrix(carros))
corr2 

#Matriz de coeficientes de correla��o
corr2$r
#Matriz de valores comparados
corr2$n
#Matriz de valores p
corr2$P

#corrplot:
corrplot(corr2$r, p.mat = corr2$P, sig.level = 0.001,
         method = 'number',
         type='upper')

#PerformanceAnalytics
install.packages("PerformanceAnalytics")
library(PerformanceAnalytics)
md = mtcars[,c(1,3,4,5,6,7)]

chart.Correlation(md, histogram = TRUE)
