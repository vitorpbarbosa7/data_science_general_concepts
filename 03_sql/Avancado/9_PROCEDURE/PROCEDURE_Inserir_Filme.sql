# Inserir novo filme

drop procedure if exists INSERIR_FILME;

select * from filme

DELIMITER $

create procedure INSERIR_FILME(filme_id smallint unsigned, 
titulo varchar(255), 
descricao text, 
ano_de_lancamento year, 
idioma_id tinyint unsigned, 
idioma_original_id tinyint unsigned, 
duracao_da_locacao tinyint unsigned, 
preco_da_locacao decimal(4,2), 
duracao_do_filme smallint unsigned, 
custo_de_substituicao decimal(5,2), 
classificacao enum('G','PG','PG-13','R','NC-17'),  
recursos_especiais set('Trailers','Commentaries','Deleted Scenes','Behind the Scenes'), 
ultima_atualizacao timestamp)

begin 

insert into filme values(filme_id, 
titulo, descricao, ano_de_lancamento, idioma_id, idioma_original_id, duracao_da_locacao, 
preco_da_locacao, duracao_do_filme, custo_de_substituicao, classificacao, recursos_especiais, ultima_atualizacao);

end
$

DELIMITER ;	

# Chamada com call à PROCEDURE de inserção de filmes

call INSERIR_FILME(1003, 'Following', 'Guy follows others', 1999, 5, 5, 2, 2.99, 90 , 20.50,'G', 'Deleted Scenes', '2020-03-03')

select * from filme where filme_id = 1003