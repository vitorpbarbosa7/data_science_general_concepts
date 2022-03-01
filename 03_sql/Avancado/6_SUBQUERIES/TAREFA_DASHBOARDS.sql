# Total de vendas do ano e do mês da locadora

# Onde temos dados de vendas?

select * from pagamento

# Total de vendas por ano:
select sum(valor), year(data_de_pagamento) ano
from pagamento 
group by ano

# Quantas vendas em cada ano?:
select count(*), year(data_de_pagamento) ano
from pagamento 
group by ano

# Média geral por ano dividindo o valor total de vendaas em R$ pelo número de vendas:
select count(*)/sum(valor), year(data_de_pagamento) ano 
from pagamento 
group by ano

# Média de pagamento por ano:
select avg(valor), year(data_de_pagamento) ano
from pagamento
group by ano

# Valor de Vendas por mês e ano 
select year(data_de_pagamento) ano, month(data_de_pagamento) mes, sum(valor)
from pagamento 
group by mes, ano

### Quero dados de vendas por mes, ano e categoria:
select * from filme
select * from filme_categoria
select * from aluguel
select * from inventario
select * from pagamento
select * from categoria

# A Query geral que foi construída para juntar pagamento com categoria através de ALUGUEL de algo no INVENTARIO, que corresponde a algum filme que está na tabela 
# FILME_CATEGORIA e esta tabela FILME_CATEGORIA possui a categoria final do filme
select p.*, a.*, i.*, f.*, c.*
from pagamento p # Onde tem o pagamento que será sumarizado
inner join aluguel a on p.aluguel_id = a.aluguel_id
inner join inventario i on a.inventario_id = i.inventario_id
inner join filme_categoria f on i.filme_id = f.filme_id
inner join categoria c on f.categoria_id = c.categoria_id # Conectar a categoria
order by p.data_de_pagamento

# Finalmente retornar qual a soma total por categoria 
select c.nome, sum(p.valor) # Soma de todas as vendas, depois agrupadas por categoria
from pagamento p # Onde tem o pagamento que será sumarizado
inner join aluguel a on p.aluguel_id = a.aluguel_id
inner join inventario i on a.inventario_id = i.inventario_id
inner join filme_categoria f on i.filme_id = f.filme_id
inner join categoria c on f.categoria_id = c.categoria_id # Conectar a categoria
group by c.nome # Nome da categoria

# Outra maneira? 
# Filme > aluguel > inventario >  Filme_Categoria

# Tabela Filme possui os valores 
# Tabela Aluguem possui o numero de vezes que aquele inventario id, aquele filme foi alugado 
# Tabelaa inventario possui 

select * from filme
select * from filme_categoria
select * from aluguel
select * from inventario
select * from pagamento
select * from categoria

# Aluguel --> Inventario --> Filme --> Filme_categoria --> Categoria
# Com essa query abaixo depois posso utilizar group by filme.preco_da_locacao
select a.*, i.*, f.*, fc.*, c.*
from aluguel a # Granularidade máxima !!!!!
inner join inventario i on a.inventario_id = i.inventario_id # Aluguel se liga com Inventario por inventario_id
inner join filme f on i.filme_id = f.filme_id # Preciso dessa parte se não não temos o [preco_da_locacao]
inner join filme_categoria fc on f.filme_id = fc.filme_id # Inventario se liga com Filme_Categoria por filme_id
inner join categoria c on fc.categoria_id = c.categoria_id # Filme Categoria se liga com Categoria por categoria_id

# O número de pagamentos condiz com o número de aalugueis? 
select count(*) from pagamento

select count(*) from aluguel
# Há uma diferença de 5 

# A outra maneira com outras tabelas, ou seja, com pagamento e não aluguel
select c.nome, sum(f.preco_da_locacao)
from aluguel a 
inner join inventario i on a.inventario_id = i.inventario_id # Aluguel se liga com Inventario por inventario_id
inner join filme f on i.filme_id = f.filme_id # Preciso dessa parte se não não temos o [preco_da_locacao]
inner join filme_categoria fc on f.filme_id = fc.filme_id # Inventario se liga com Filme_Categoria por filme_id
inner join categoria c on fc.categoria_id = c.categoria_id # Filme Categoria se liga com Categoria por categoria_id
group by c.nome

# O resultado foi diferente, utilizando aluguel ou pagamento, então não sei 

# Agrupar por ano e mes 
select year(a.data_de_aluguel) ano, month(a.data_de_aluguel) mes, c.nome nome, sum(f.preco_da_locacao)
from aluguel a 
inner join inventario i on a.inventario_id = i.inventario_id # Aluguel se liga com Inventario por inventario_id
inner join filme f on i.filme_id = f.filme_id # Preciso dessa parte se não não temos o [preco_da_locacao]
inner join filme_categoria fc on f.filme_id = fc.filme_id # Inventario se liga com Filme_Categoria por filme_id
inner join categoria c on fc.categoria_id = c.categoria_id # Filme Categoria se liga com Categoria por categoria_id
group by ano, mes, nome