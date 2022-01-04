# 
DROP PROCEDURE IF EXISTS PROC1;

DELIMITER $

create procedure PROC1()

begin 

# Ação a ser realizada

# No caso vou chamar uma função como ação
# Uma função soma já criada, com dois parâmetros
# O resultado da função será chamado de CONTA
# O número de parâmetros tem que bater
select soma (10,20) as 'CONTA';

end
$

DELIMITER ;


call PROC1()
