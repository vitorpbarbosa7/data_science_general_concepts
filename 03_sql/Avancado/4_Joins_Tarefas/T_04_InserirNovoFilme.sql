-- Inserir novo filme

-- Descrição dos tipos de dados
desc filme

select * from filme limit 2;

insert into filme (filme_id, titulo, descricao, ano_de_lancamento, idioma_id, idioma_original_id, duracao_da_locacao, preco_da_locacao, duracao_do_filme, custo_de_substituicao, classificacao, recursos_especiais, ultima_atualizacao)
values
(null,"FOLLOWING", "A lost guy follows others in the streets the discover things about their lifes", 1999, 1,null,6,10.99,50,17.99,'G',null,'2006-02-15 05:03:01')

-- Verificar o novo registro
select *
from filme
where titulo = 'FOLLOWING'

-- ENUM não aceita novos dados mesmo
insert into filme (filme_id, titulo, descricao, ano_de_lancamento, idioma_id, idioma_original_id, duracao_da_locacao, preco_da_locacao, duracao_do_filme, custo_de_substituicao, classificacao, recursos_especiais, ultima_atualizacao)
values
(null,"FOLLOWING", "A lost guy follows others in the streets the discover things about their lifes", 1999, 1,null,6,10.99,50,17.99,'AA',null,'2006-02-15 05:03:01')

-- SET não aceita novos dados mesmo
insert into filme (filme_id, titulo, descricao, ano_de_lancamento, idioma_id, idioma_original_id, duracao_da_locacao, preco_da_locacao, duracao_do_filme, custo_de_substituicao, classificacao, recursos_especiais, ultima_atualizacao)
values
(null,"FOLLOWING", "A lost guy follows others in the streets the discover things about their lifes", 1999, 1,null,6,10.99,50,17.99,'G','newnew','2006-02-15 05:03:01')

-- Dá duplicate da linha se colocar um que já existe? provavelmente sim se um dos campos for autoincremental ou unique constraint
insert into filme (filme_id, titulo, descricao, ano_de_lancamento, idioma_id, idioma_original_id, duracao_da_locacao, preco_da_locacao, duracao_do_filme, custo_de_substituicao, classificacao, recursos_especiais, ultima_atualizacao)
values
('2', 'ACE GOLDFINGER', 'A Astounding Epistle of a Database Administrator And a Explorer who must Find a Car in Ancient China', 2006, '1', NULL, '3', '4.99', '48', '12.99', 'G', 'Trailers,Deleted Scenes', '2006-02-15 05:03:42')