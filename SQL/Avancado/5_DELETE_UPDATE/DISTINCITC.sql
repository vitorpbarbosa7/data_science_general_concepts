select * from filme

select distinct duracao_da_locacao
from filme

-- Utilizar Distinct e Group by para retornar apenas títulos não duplicados
-- Aqui fica duplicado por causa da data, afinal um filme pode ser alugado em mais de uma data
-- Vamos retirar a data do select porque não faz sentido utiliar a data no distinct e group by

select distinct fil.titulo, fil.*
from aluguel as alu
inner join inventario as inv on alu.inventario_id = inv.inventario_id
inner join filme as fil on inv.filme_id = fil.filme_id

-- Com Group By
select fil.titulo, fil.*
from aluguel as alu
inner join inventario as inv on alu.inventario_id = inv.inventario_id
inner join filme as fil on inv.filme_id = fil.filme_id
group by fil.titulo