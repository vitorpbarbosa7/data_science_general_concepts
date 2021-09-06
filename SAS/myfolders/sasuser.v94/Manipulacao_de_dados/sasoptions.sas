data salaryemp;
infile '/folders/myfolders/sasuser.v94/salary.txt';
input year salary;
run;

/* Retornar apenas uma coluna */
data salaryemp(keep=salary);
infile '/folders/myfolders/sasuser.v94/salary.txt';
input year salary;
run;

/* Renomear salario */
data salaryemp(keep=salary rename=salary=salaryemp);
infile '/folders/myfolders/sasuser.v94/salary.txt';
input year salary;
run;

proc print data=saralyemp(obs=4);
run;


/* Procedure para imprimir apenas algumas observações */
data salaryemp(keep=salary rename=salary=salaryemp);
infile '/folders/myfolders/sasuser.v94/salary.txt';
proc print data=saralyemp(obs=4);
run;