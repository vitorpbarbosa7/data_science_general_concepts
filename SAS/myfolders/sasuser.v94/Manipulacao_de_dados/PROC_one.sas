/* Comentário no SAS */

/* Como importar com uma PROCEDURE 
para importar dados*/

proc import out=salesdata datafile="/folders/myfolders/sasuser.v94/Sample-Sales-Data.xlsx" dbms=xlsx REPLACE;
sheet="Sheet1"; *para selecionar apenas a sheet desejada;
delimiter=";";
getnames=yes; *Pegar o título;

run;

