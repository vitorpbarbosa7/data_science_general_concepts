select * from filme

# Função nova para trabalhar com texto

# Id vai ser a variável para se trabalhar com a chave primária da base

DELIMITER $$
create function `nome` (id integer)
returns varchar(200)

begin

declare nome varchar(200);

# Into para dizer onde colocar o resultado desse select
#  A variável que recebe do into é a variável que será retornada
select descricao into nome from filme where filme_id = id;

return nome;

end $$

DELIMITER ;

select nome(50)

