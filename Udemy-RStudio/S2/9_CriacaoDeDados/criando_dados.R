#Função rep que permite replicar valores de uma lista ou vetor
?rep

vetor = rep("abc",3)

times = rep(c("a", "b", "c"), times=3)
each = rep(c("a", "b", "c"), each=3)

eachtimes = rep(c("a","b","c"), each=3, times=3)

#Função sample
#Mas quantos? 
sample(1:10,5)

#Determinando a semente:
set.seed(0)
#Deve ser executada em conjunto para funcionar. 
sample(1:10,3)

set.seed(22)

#Função replace no sample
amostra = sample(1:5,100,replace = T)

plot(amostra)

hist(amostra)

df = data.frame("a" = 1:5, b = c(1,5,9,7,8))
                