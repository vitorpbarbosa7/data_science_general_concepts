select *
from aluguel

select * 
from cliente

-- Join aluguel with cliente by cliente_id

select a.*, b.*
from aluguel as a 
inner join cliente as b on a.cliente_id = b.cliente_id

-- Valor gasto em aluguel por cliente (Já tem uma base, não vai precisar de inner join)
select cliente_id, sum(valor) as valor_total
from pagamento
group by cliente_id
order by valor_total desc

-- Número de clientes por cidade? 
-- Esse talvez seja um problema legal 
select *
from cidade

-- Join bonitinho
select c.*, e.endereco_id, cli.primeiro_nome, cli.ultimo_nome, cli.email, cli.ativo
from cidade as c
left join endereco as e on c.cidade_id = e.cidade_id
left join cliente as cli on e.endereco_id = cli.endereco_id

-- Essa query retornou 604 linhas
-- Mas quantos clientes existem? 

select count(*)
from cliente

-- Só existem 599 clientes

-- Quantas cidades existem? 
select count(*)
from cidade

-- Checar por duplicata de clientes na tabela criada?
select distinct cli.cliente_id
from cidade as c
left join endereco as e on c.cidade_id = e.cidade_id
left join cliente as cli on e.endereco_id = cli.endereco_id


-- Contar quantos clientes existem por cidade
select c.cidade, sum(cli.cliente_id) as clientes_por_cidade
from cidade as c
left join endereco as e on c.cidade_id = e.cidade_id
left join cliente as cli on e.endereco_id = cli.endereco_id
group by c.cidade_id
order by clientes_por_cidade desc
