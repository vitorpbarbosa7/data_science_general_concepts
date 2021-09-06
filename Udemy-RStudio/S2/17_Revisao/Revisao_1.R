setwd("C:\\Users\\Vitor Barbosa\\Google Drive\\DS\\Udemy-R\\S2\\17_Revisao")

# Código para limpeza da tela
cat("\014")

#Código para limpar a variable explorer
rm(list=ls())

data()

View(ChickWeight)

?ChickWeight
frango = ChickWeight

View(frango)

?str
str(frango)

#Histograma
hist(frango$weight, freq = F,xlab = "Peso")
abline(v=mean(frango$weight),lty=2)
mean((frango$weight))
median(frango$weight)
#Add vertical line:
?abline
example(abline)

#Correlação:
library(corrplot)

carros = mtcars

carrocorrelacao = cor(carros)

corrplot(carrocorrelacao, method = 'shade')

correlacao = cor(frango)
correlacao

plot(frango$Time,frango$weight)

#É possível retornar boxplot a partir do plot:
plot(frango$Diet, frango$weight)
plot(frango$Diet, frango$Time)

#Boxplot:
boxplot(frango$weight)

names(frango)
?ChickWeight
#Função table:
table(frango$Time)
table(frango$Diet)
mean(frango$weight)
sd(frango$weight)

#$Barplot e tapply é ótimo
barplot(tapply(frango$weight,frango$Diet,mean))
abline(h=mean(frango$weight, lty=2))

barplot(tapply(frango$weight, frango$Time, mean))
abline(h=mean(frango$weight), lty=1)

#Teste estatístico
x1 = frango[frango$Diet==1,]
x2 = frango[frango$Diet==2,]
x3 = frango[frango$Diet==3,]
x4 = frango[frango$Diet==4,]

#Nas dietas 1 e 2
t.test(x1$weight,x3$weight)

t.test(x3$weight,x4$weight)
