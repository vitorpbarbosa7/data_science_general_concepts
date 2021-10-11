/* Definição das variáveis de ambiente para encontrar o python e o R */

OPTIONS SET = R_HOME 'C:\R-4.0.4\';
OPTIONS SET = PYTHONHOME 'C:\Users\vitor\anaconda3';

/* Iniciar a Procedure para o R */
Proc R;
submit;

First_Name = c("Jordan","Larry","Sarah")
Last_Name = c("Latner","Benner","Gabriela")
df = data.frame(First_Name, Last_Name, Age)

print(df)
endsubmit;
run;