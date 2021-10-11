data beer;
input brand$ origin$ price;
cards; /* Há linhas de dados que serão inseridas a seguir nas próximas linhas */
Budweiser USA 14.99
Heineken NED 13.99
Corona MEX 12.99
SamAdams USA 14.79
Guinness IRE 17.99
;

/* Fixed formatted data */
data beer;
input brand$ 1-9 origin$ 10-12 price 13-17;
cards;
BudweiserUSA14.99
HeinekenNED13.99
CoronaMEX12.99
SamAdamsUSA14.79
GuinnessIRE17.99
;