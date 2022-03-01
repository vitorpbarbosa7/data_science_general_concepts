select * from filme

# Função nova para trabalhar com texto

# Id vai ser a variável para se trabalhar com a chave primária da base

DELIMITER $$
create function `like_placeholder` (caracteres varchar(200))
returns varchar(200)

begin

declare nome varchar(200);

# Into para dizer onde colocar o resultado desse select
#  A variável que recebe do into é a variável que será retornada
select titulo into nome from filme where titulo like caracteres;

return nome;

end $$

DELIMITER ;

select like_placeholder('AC%')

select * from filme

