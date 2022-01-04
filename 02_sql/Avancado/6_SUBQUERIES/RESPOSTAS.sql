#Listagem da descrição dos Filmes em Ordem Alfabética 
#Ascendente
Select *
from filme
order by descricao asc;

#Descendente
Select *
from filme
order by descricao desc;


#Joins de Tabelas
Select * 
from aluguel;

select *
from cliente;

select b.primeiro_nome, b.ultimo_nome, b.email, count(*)
from aluguel a, cliente b
where  a.cliente_id = b.cliente_id
group by b.primeiro_nome
order by b.primeiro_nome;


#Localize os filmes de sua loja virtual como gênero Ação
# categoria_id = 1 (Action)
Select *
from categoria;

select *
from filme;

select *
from filme_categoria;


select a.nome, b.titulo, b.descricao, b.preco_da_locacao
from categoria a,filme b, filme_categoria c
where a.categoria_id = c.categoria_id
and b.filme_id = c.filme_id
and a.categoria_id = 1
order by 4;


# Procure o último Filme alugado de sua Locadora
# A ligação com Filme está na tabela de inventario
# Ultima data_de_aluguel da tabela aluguel
select * from aluguel;

select * from inventario;

select * from filme;

select a.data_de_aluguel, c.titulo, c.descricao, c.filme_id, a.aluguel_id
from aluguel a, inventario b, filme c
where a.inventario_id = b.inventario_id
and b.filme_id = c.filme_id
and c.filme_id = 2
and a.aluguel_id =  13421
order by data_de_aluguel desc;


#Somando valores com o comando SUM
select sum(a.preco_da_locacao)
from filme a;

select a.nome,sum(b.preco_da_locacao), sum(custo_de_substituicao)
from categoria a,filme b, filme_categoria c
where a.categoria_id = c.categoria_id
and b.filme_id = c.filme_id;

#Recuperando a Média dos valores de uma tabela usando AVG()
select avg(a.preco_da_locacao)
from filme a;

select a.nome,avg(b.preco_da_locacao), avg(custo_de_substituicao)
from categoria a,filme b, filme_categoria c
where a.categoria_id = c.categoria_id
and b.filme_id = c.filme_id;

#Filtrando ocorrências duplicadas pela cláusula DISTINCT
select distinct c.titulo, c.descricao, c.filme_id
from aluguel a, inventario b, filme c
where a.inventario_id = b.inventario_id
and b.filme_id = c.filme_id
order by data_de_aluguel desc;


#Mão na Massa - Traga um filme distinto em registros repetidos
select distinct c.titulo, c.descricao, c.filme_id
from aluguel a, inventario b, filme c
where a.inventario_id = b.inventario_id
and b.filme_id = c.filme_id
order by data_de_aluguel desc;


select c.titulo, c.descricao, c.filme_id
from aluguel a, inventario b, filme c
where a.inventario_id = b.inventario_id
and b.filme_id = c.filme_id
group by c.titulo, c.descricao
order by data_de_aluguel desc;


#Cláusula HAVING()
select b.primeiro_nome, b.ultimo_nome, b.email, count(*) total_de_alugueis
from aluguel a, cliente b
where  a.cliente_id = b.cliente_id
group by b.primeiro_nome
having count(*)<20
order by 4;

#SUBCONSULTAS
select * from endereco c where c.endereco_id 
in (select b.endereco_id
from aluguel a, cliente b
where  a.cliente_id = b.cliente_id
group by b.primeiro_nome
having count(*)<20);

select max(c.data_de_aluguel) from aluguel c where c.aluguel_id 
in (select a.aluguel_id
from aluguel a, cliente b
where  a.cliente_id = b.cliente_id
group by b.primeiro_nome
having count(*)<20);


#TUNING 
select a.nome, b.titulo, b.descricao, b.preco_da_locacao
from categoria a,filme b, filme_categoria c
where a.categoria_id = c.categoria_id
and b.filme_id = c.filme_id
AND b.filme_id = 19
order by 4;
    

# Dashboards
select a.nome, sum(b.preco_da_locacao) preco_da_locacao
from categoria a,filme b, filme_categoria c
where a.categoria_id = c.categoria_id
and b.filme_id = c.filme_id
group by a.nome;

#Mão na Massa - Faça um Dashboard com o total de vendas do ano e do mês de sua locadora

#VENDAS MENSAIS
select d.nome Categoria, sum(b.preco_da_locacao) preco_da_locacao
from aluguel a, filme b, inventario c, categoria d, filme_categoria e
where a.data_de_devolucao between "2005-05-01 00:00:00" and  "2005-05-31 23:59:59"
and a.inventario_id = c.inventario_id
and b.filme_id = c.filme_id
and d.categoria_id = e.categoria_id
and e.filme_id = b.filme_id
group by d.nome;


#VENDAS ANUAL
select d.nome Categoria, sum(b.preco_da_locacao) preco_da_locacao
from aluguel a, filme b, inventario c, categoria d, filme_categoria e
where a.data_de_devolucao between "2005-01-01 00:00:00" and  "2005-12-31 23:59:59"
and a.inventario_id = c.inventario_id
and b.filme_id = c.filme_id
and d.categoria_id = e.categoria_id
and e.filme_id = b.filme_id
group by d.nome;

















