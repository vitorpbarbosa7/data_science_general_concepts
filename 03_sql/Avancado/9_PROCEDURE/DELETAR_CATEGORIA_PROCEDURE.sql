# Deletar categoria

select * from categoria

DELIMITER $

create procedure DELETA_CATEGORIA(p_id integer)

begin 

# Deletar a linha inteira com procedure
delete from categoria where categoria_id = p_id;

end
$

DELIMITER ;

# Não deixava deletar se houvesse foreign key, ou seja, ligação dessa chave com outras tabelas
call DELETA_CATEGORIA(17);
