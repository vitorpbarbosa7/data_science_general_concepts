data houseprice;
infile '/folders/myfolders/sasuser.v94/houseprice.txt';
input type$ price tax;

/* Como adicionar nova variável */

actual_amount_tax = round(price*tax);

/* Outras maneiras de aadicionar novas variaveis */

data sales;
input name$ sales_1-sales_4;
total = (sales_1 + sales_2 + sales_3 + sales_4);
cards;
Greg 10 2 40 0
John 15 5 10 100
Lise 50 10 15 50
Mark 20 0 5 20
;
