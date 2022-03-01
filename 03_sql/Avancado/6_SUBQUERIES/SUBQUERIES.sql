select * from filme

# Encontrar registros que se encontram o valor mínimo de preço de locação 

select titulo, descricao, ano_de_lancamento, preco_da_locacao
from filme 
where preco_da_locacao = (select min(preco_da_locacao) from filme) 

select titulo, descricao, ano_de_lancamento, preco_da_locacao
from filme 
where preco_da_locacao = (select max(preco_da_locacao) from filme) 

select titulo, descricao, ano_de_lancamento, preco_da_locacao
from filme 
where preco_da_locacao = (select avg(preco_da_locacao) from filme) 

# Retornar filmes que tenham sua duração próximo à média
select titulo, descricao, ano_de_lancamento, duracao_do_filme
from filme
where duracao_do_filme between 114 and 116

select titulo, descricao, ano_de_lancamento, duracao_do_filme
from filme
where duracao_do_filme = 115

select avg(duracao_do_filme) from filme

# Retornar filmes que tenham a duracao minima
select titulo, descricao, ano_de_lancamento, duracao_do_filme
from filme
where duracao_do_filme =
(select min(duracao_do_filme) from filme)

# Retornar filmes que tenham a duracao máxima
select titulo, descricao, ano_de_lancamento, duracao_do_filme
from filme
where duracao_do_filme =
(select max(duracao_do_filme) from filme)



