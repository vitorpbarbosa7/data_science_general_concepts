data salary;
infile '/folders/myfolders/sasuser.v94/salary.txt';
input year salary;

/* Quando o delimitador é diferente */
data salary2;
infile '/folders/myfolders/sasuser.v94/salary2.txt' DLM=";";
input year salary;


