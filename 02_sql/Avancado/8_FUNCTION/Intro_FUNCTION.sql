# Para me deixar criar uma função boba, ou seja, uma função que já existe, a função soma
set global log_bin_trust_function_creators = 1;

# Mudar o delimiter para ele considerar toda o código abaixo sem parar a sua execução no ;
DELIMITER $$

# Criação da estrutura geral da função
# Esta ainda não é uma STORED PROCEDURE, ou seja, um procedicmento armazenado, mas é análogo

create function `soma` (num1 decimal(8,2), num2 decimal(8,2))
returns decimal(8,2) # Return tipo de variável

begin

# A variável que irá receber o resultado da operação executada na função
declare total decimal(8,2); 

# Qual operação realizar e em qual variável atribuir o seu resultado
set total = num1 + num2; 

# Return a variável 
return total; 

end $$

# Voltando o delimitador para o ; após a criação da STORED PROCEDURE
DELIMITER ;

# Agora vamos executar a função que criamos
select soma(20,22)

