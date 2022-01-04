select *
from aluguel

select distinct a.cliente_id, cli.primeiro_nome, cli.ultimo_nome
from aluguel as a
inner join cliente as cli on a.cliente_id = cli.cliente_id