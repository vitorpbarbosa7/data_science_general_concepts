-- Like and in together only with or statements

select * 
from cliente

select * 
from cliente 
where primeiro_nome LIKE '%SA%'
OR primeiro_nome LIKE '%TA%'
OR primeiro_nome LIKE '%FA%'