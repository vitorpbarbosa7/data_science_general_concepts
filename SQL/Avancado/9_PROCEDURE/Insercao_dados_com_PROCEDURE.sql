# Inserção de dados com PROCEDURE

select * from categoria

# Cadastro de categoria

DELIMITER $

create procedure CAD_CATEGORIA(p_id int(10), p_nome varchar(30), p_data timestamp)

begin

insert into categoria values (p_id, p_nome, p_data);

end
$

DELIMITER ;

call CAD_CATEGORIA(17, 'Psicologia Profunda', '2005-03-03')

