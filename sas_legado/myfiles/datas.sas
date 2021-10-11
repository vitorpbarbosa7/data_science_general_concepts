/* Ler datas em dados */

data dates;

/* Você tem que printar o nome o aniversário das pessoas */

input name$ bday date11.;
cards;
Thais 19 May 1996
Vitor 7 Jul 1993
Andre 1 Jul 1993
Fabio 13 Apr 1992
;

/* Códigos adicionais para fazer essa merda funcionar */

proc print data=dates;
format bday date9.;

