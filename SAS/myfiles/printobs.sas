/* Renomear salario */
data salaryemp(keep=salary rename=salary=salaryemp);
infile '/folders/myfolders/sasuser.v94/salary.txt';
input year salary;
run;

proc print data=saralyemp(obs=4);
run;