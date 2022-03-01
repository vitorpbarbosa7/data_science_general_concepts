-- Mostrar o último filme alugado na locadora

select *
from filme

select * 
from inventario

select *
from pagamento

select *
from aluguel
order by data_de_aluguel desc

-- Aluguel se liga com inventario com inventario
-- Inventario se liga com filme com filme_id

select alu.data_de_aluguel, alu.data_de_devolucao, fil.*
from aluguel as alu
inner join inventario as inv on alu.inventario_id = inv.inventario_id
inner join filme as fil on inv.filme_id = fil.filme_id
order by alu.data_de_aluguel desc

