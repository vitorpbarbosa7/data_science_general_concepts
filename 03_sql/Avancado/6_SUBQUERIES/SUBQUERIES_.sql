select * from cliente

# Quais endereços dos clientes que alugaram menos que 20 filmes?

select * from endereco as endr where endr.endereco_id in
(select cli.endereco_id
from cliente as cli
inner join aluguel as alu on cli.cliente_id = alu.cliente_id
group by cli.cliente_id
having count(*) < 20)

# CO




