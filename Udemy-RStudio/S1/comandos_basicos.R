# cerquilha/jogo-da-velha/hash utilizado para fazer coment√°rios, o c√≥digo n√£o √© lido pelo console do R
# aspas "" e '' tamb√©m para coment√°rios

#Coment·rios
"Coment·rio colorido"
"coment√°rio aleat√≥rio"

# aspas s√£o utilizadas tamb√©m em fun√ß√µes

#Comandos b√°sicos no R
1+1
2-1
3*4
6/3

2^3

5 %/%2 #divis√£o de n√∫meros inteiros

2+1==3 #verdadeiro
2==3 #falso

2<=3
2>=3

# "<-" e "=" utilizados para criar objetos 
#Maneira estranha de atribuir valor a uma vari·vel
x<- 5

x+2
#Maneira normal de criar uma vari·vel, n„o aquela estranha
x = 4

# () par√™nteses s√£o utilizados em fun√ß√µes
funcao£o(argumento,argumento)

"FunÁ„o mais b·sica do R È essa funÁ„o chamada c"
x= c(1,2,3) # c √© uma fun√ß√£o para concatenar elementos
# se tudo estiver em parentesis o R 'imprime' o objeto

"Ao colocar o cÛdigo entre parÍnteses ele vai imprimir"
(x<- c(1,2,3))
x
"Algumas precisaam realmente do print"
print(x)

x #erro

# : algo como "at√©"
"Dois pontos (:) no R funciona como se fosse um 'atÈ'"
1:20
"IndexaÁ„o em R È 1?"
x<- 20:30

# [] d√° acesso aos elementos de um objeto

"Colchetes fofinhos igual Python"
x[3]

# Operadores l√≥gicos
"Slices fofinhos, me retorne x maior que 25 e x menor que 25"
x[x>25]
x[x<25]

"S„o operadores lÛgicos"
x[x>22 & x<28] # x maior que 22 E menor que 28
"Ou em R È | a famosa barra retona"
x[x<23 | x>27] # x menor que 23 OU maior que 27

x[x>22 & x!=28]

# fun√ß√µes dentro de fun√ß√µes
# algo semelhante a opera√ß√µes aritm√©ticas
x+ 1
(x+1)* 2

plot(x)
plot(x^10)
log(x)
plot(log(x))

