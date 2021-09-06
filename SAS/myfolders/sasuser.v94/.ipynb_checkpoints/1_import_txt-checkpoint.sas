DATA weightgain;

INFILE "/folders/myfolders/sasuser.v94/weightgain.csv" DSD MISSOVER FIRSTOBS=2

/* Nome das colunas de acordo com o número de colunas e suas posições no arquivo original */;

INPUT id source type weightg; 

RUN;

