# Vamos aprender a fazer melhores queries

select * from inventario
-- Sempre utilizar os índices no SELECT, para melhorar a performance do retorno da query
-- Colocar apelido nas tabelas, apelidos, alias, curtos
-- Colocar no WHERE números e não textos

# Retornar nome, titulo, descricao e preco da locacao dos filmes
select a.nome, b.titulo, b.descricao, b.preco_da_locacao 
from categoria a, filme b, filme_categoria c
where a.categoria_id = c.categoria_id
and b.filme_id = c.filme_id
order by b.preco_da_locacao

# Mesma coisa com número:
select a.nome, b.titulo, b.descricao, b.preco_da_locacao 
from categoria a, filme b, filme_categoria c
where a.categoria_id = c.categoria_id
and b.filme_id = c.filme_id
order by 4


