data A;
do i = 1 to 5;
y = i*2;
output;
end;

/* While */

data A;
do i = 1 to 5 while (y < 15);
y = i*2;
output;
end;

/* determinar os valores */

data A;
do v = 1,5,9,10,15;
y = v*2;
output;
end;
run;

/* outra */
data A;
input years;
datalines;
4
5
6
7
8
9
;

data B; /* novos dados */
set A; /* utilizando dados anteriores */
if years > 5 then 
do;
months = years*12;
put years = months=;
end;
else yrsleft=5-years;







