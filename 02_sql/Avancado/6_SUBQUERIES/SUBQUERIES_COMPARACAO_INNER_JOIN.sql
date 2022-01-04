select * from cliente

# Quais endereços dos clientes que alugaram menos que 20 filmes?

select * from endereco as endr where endr.endereco_id in
(select cli.endereco_id
from cliente as cli
inner join aluguel as alu on cli.cliente_id = alu.cliente_id
group by cli.cliente_id
having count(*) < 20)

# Com Inner Join:
select * from endereco as endr 
inner join
(select cli.endereco_id
from cliente as cli
inner join aluguel as alu on cli.cliente_id = alu.cliente_id
group by cli.cliente_id
having count(*) < 20) as aux on endr.endereco_id = aux.endereco_id

# Qual a última data de locação?]
select * from cliente 

select * from aluguel

select max(data_de_aluguel) from aluguel where data_de_aluguel in
(select alu.data_de_aluguel
from cliente as cli
inner join aluguel as alu on cli.cliente_id = alu.cliente_id
group by cli.cliente_id
having count(*) < 20)

