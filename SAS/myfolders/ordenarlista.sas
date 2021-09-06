data houseprice;
input type$ price tax;
CARDS;
Single 300000 0.20
Single 250000 0.25
Duplex 175000 0.15
;
RUN;

proc print data=houseprice;
run;

proc sort data=houseprice out=houseprice2;
by tax;
run;

proc print data=houseprice2;
run;