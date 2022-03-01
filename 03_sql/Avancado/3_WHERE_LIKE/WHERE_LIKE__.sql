select *
from cliente
where ativo = 0

select * 
from cliente
where primeiro_nome like '%san%'

select *
from cliente 
where email like "%sa%"

select * 
from cliente 
where loja_id in (1,2,3)

select loja_id, count(loja_id)
from cliente
group by loja_id

select *
from cliente 
where ultimo_nome in (