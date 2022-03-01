 select  classificacao, count(classificacao)
from filme
group by classificacao

select duracao_da_locacao, count(duracao_da_locacao)
from filme
group by duracao_da_locacao