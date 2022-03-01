-- Localizar filmes de genero de ação 

select * 
from filme

select * 
from filme_categoria

select *
from categoria

select filme.filme_id, filme.titulo, cat.nome
from categoria as cat
inner join filme_categoria as fil_cat on cat.categoria_id = fil_cat.categoria_id
inner join filme on fil_cat.filme_id = filme.filme_id
where cat.nome = 'Action'



