data houseprice;
infile '/folders/myfolders/sasuser.v94/Manipulacao_de_dados/data/houseprice.txt';
input type$ price tax;
run;

data newhomes;
infile '/folders/myfolders/sasuser.v94/Manipulacao_de_dados/data/newhomes.txt';
input type$ price tax;

proc sort data=houseprice out=houseprice2;
by price;
run;

proc sort data=newhomes out=newhomes2;
by price;
run;