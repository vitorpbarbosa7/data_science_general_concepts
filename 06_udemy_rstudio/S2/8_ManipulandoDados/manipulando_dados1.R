#Visualizar os dados

dados=read.csv("dados1.csv")

View(dados)
head(dados)
names(dados)
str(dados)

#Acessar os campos
dados[2,3]
dados[,3]
dados[1,]
dados[5,]

#Acessar colunas específicas
dados$genero
dados$peso
dados$
  
#Não funcionou brow 
dados[,"peso"]

#Média de algum específico
mean(dados$peso)

#Filtragem de dados

dados$genero

#Objeto feminino 
Feminino <- dados[dados$genero == "feminino",]

View(Feminino)

altos = dados[dados$altura > 1.6,]
View(altos)

dados_drop_column = dados[,-3]
