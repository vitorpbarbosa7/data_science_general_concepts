data sales;
input name$ sales_1-sales_4;
total=sales_1+sales_2+sales_3+sales_4;
if name = 'Greg' THEN total = 0;
cards;
Greg 10 2 40 0
John 15 5 10 100
Lisa 50 10 15 50 
Mark 20 0 5 20
;

data sales;
input name$ sales_1-sales_4;
total=sales_1+sales_2+sales_3+sales_4;
Fired = '';
IF name = 'Greg' AND total=>52 THEN 
DO;
Fired = 'N';
total = total + 10;
END; /* Fechar a merda do DO */
cards;
Greg 10 2 40 0
John 15 5 10 100
Lisa 50 10 15 50 
Mark 20 0 5 20
;



