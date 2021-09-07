setwd("C:\\Users\\Vitor Barbosa\\Google Drive\\DS\\Udemy-R\\S2\\10_ManipularDados2")

# Código para limpeza da tela
cat("\014")

#Código para limpar a variable explorer
rm(list=ls())

laranja = Orange

laj = data.frame("Tree" =  as.factor(rep(c(6,7),each=7)),
                "age" =  rep(c(118,484,664,1004,1231,1372,1582),times = 2),
                "circumference" = c(30,60,90,120,130,140,150,25,050,70,80,90,100,115))

laj1 = data.frame("Tree" = laranja$Tree, "idade_quadrada" = laranja$age^2)

laj2 = data.frame("Arvore" = laranja$Tree, "idade_quadrada" = laranja$age^2)


#Unir dataframes:
#Por linhas
linhas = rbind(laranja, laj)
#Por colunas
colunas = cbind(laranja, laj1)

#Pode ser que não precise escrever por onde realizar a fusão
fusao = merge(laranja, laj1)

#Especificando por onde realizar a fusão:
fusao2 = merge(laranja, laj1, by="Tree")

#Se houveressem nomes diferentes nestes dataframes:
fusao3 = merge(laranja, laj2, by.x = "Tree", by.y = "Arvore")

#Contar variáveis:
dados1 = read.csv("dados1.csv")

table(laranja$age)

table(dados1$peso)

hist(dados1$peso, freq = F)

tabledf = data.frame(table(laranja$age))

