data houseprice;
infile '/folders/myfolders/sasuser.v94/houseprice.txt';
input type$ price tax;

proc standard data=houseprice mean=0 std=1 out=standardnew;
var price tax;

proc means data=standardnew;

/* Outra maneira de fazer isso criando nova tabela */

data houseprice2; /* Novos dados */
set houseprice; /* Referenciar aos dados anteriores */
/* Standardized price (sprice) and Standardized tax (stax) */
sprice = price;
stax = tax;

proc standard data=houseprice2 mean = 0 std = 1 out = standardnew;
var sprice stax; /*Executar apenas nestes para exibir os que não estão assim padronizados */
proc means data=standardnew;


