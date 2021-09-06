
# Como retornar todos os filmes com o menor preço de locação:

# Filmes com menor preço de locação
# Utilizando Subquery

create view relatorio_filme_min_preco_locacao as 
select titulo, descricao, preco_da_locacao
from filme
where preco_da_locacao = 
(select min(preco_da_locacao)
from filme)

# Uma View é uma subset de um select

# Mas uma view sempre é mais lenta que um select
# Porque é uma tabela não verdadeira, que é um select de um select, 
# Perdemos performance
select * from relatorio_filme_min_preco_locacao

-- A View aparece até mesmo no show tables
show tables

####
# Finalmente retornar qual a soma total por categoria 
# A outra maneira com outras tabelas, ou seja, com pagamento e não aluguel

create view v_relatorio_vendas_mes_ano as 
select year(a.data_de_aluguel) ano, month(a.data_de_aluguel) mes, c.nome categoria, sum(f.preco_da_locacao) total_vendas
from aluguel a 
inner join inventario i on a.inventario_id = i.inventario_id # Aluguel se liga com Inventario por inventario_id
inner join filme f on i.filme_id = f.filme_id # Preciso dessa parte se não não temos o [preco_da_locacao]
inner join filme_categoria fc on f.filme_id = fc.filme_id # Inventario se liga com Filme_Categoria por filme_id
inner join categoria c on fc.categoria_id = c.categoria_id # Filme Categoria se liga com Categoria por categoria_id
group by ano, mes, categoria

# Consigo fazer DML em view? 
delete from v_relatorio_vendas_mes_ano where categoria = 'Action'

/*However, to create an updatable view, the SELECT statement that defines the view must not contain any of the following elements:

Aggregate functions such as MIN, MAX, SUM, AVG, and COUNT.
DISTINCT
GROUP BY clause.
HAVING clause.
UNION or UNION ALL clause.
Left join or outer join.
Subquery in the SELECT clause or in the WHERE clause that refers to the table appeared in the FROM clause.
Reference to non-updatable view in the FROM clause.
Reference only to literal values.
Multiple references to any column of the base table.*/

### ALTER VIEW

alter view v_relatorio_vendas_mes_ano as 
select year(a.data_de_aluguel) year_, month(a.data_de_aluguel) month_, c.nome category, sum(f.preco_da_locacao) sum_selling
from aluguel a 
inner join inventario i on a.inventario_id = i.inventario_id # Aluguel se liga com Inventario por inventario_id
inner join filme f on i.filme_id = f.filme_id # Preciso dessa parte se não não temos o [preco_da_locacao]
inner join filme_categoria fc on f.filme_id = fc.filme_id # Inventario se liga com Filme_Categoria por filme_id
inner join categoria c on fc.categoria_id = c.categoria_id # Filme Categoria se liga com Categoria por categoria_id
group by year_, month_, category

select * from v_relatorio_vendas_mes_ano

### Create or update view 

create or replace view v_relatorio_vendas_mes_ano as 
select year(a.data_de_aluguel) __year__, month(a.data_de_aluguel) __month__, c.nome category, sum(f.preco_da_locacao) sum_selling
from aluguel a 
inner join inventario i on a.inventario_id = i.inventario_id # Aluguel se liga com Inventario por inventario_id
inner join filme f on i.filme_id = f.filme_id # Preciso dessa parte se não não temos o [preco_da_locacao]
inner join filme_categoria fc on f.filme_id = fc.filme_id # Inventario se liga com Filme_Categoria por filme_id
inner join categoria c on fc.categoria_id = c.categoria_id # Filme Categoria se liga com Categoria por categoria_id
group by __year__, __month__, category


# DROP VIEW

drop view v_relatorio_vendas_mes_ano

# Show tables para ver que a View foi dropada com sucesso
show tables