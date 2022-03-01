drop procedure if exists PROC2;

DELIMITER $

create procedure PROC2(num1 decimal, num2 decimal, num3 decimal, num4 decimal)

begin 

select soma (num1, num2, num3, num4) as 'conta';

end
$

DELIMITER ;

# Para funcionar, os argumentos da função e da procedure devem bater em questão de número (aqui de num1 até num4)
call PROC2(1,2,3,4);
