# Criar função que retorne o número de elementos em um banco de dados

# Permitir a criação de função boba que já existe
set global log_bin_trust_function_creators = 1;

DELIMITER $$
# Função sem parâmetros
create function `contar_elementos` ()
# Aqui é returnS
returns integer

# NÃO ESQUECER DO PONTO E VÍRGULA
# NÃO ESQUECER DO PONTO E VÍRGULA
# NÃO ESQUECER DO PONTO E VÍRGULA
begin

declare contagem integer;

select count(*) into contagem from filme;

# Retornar a variável contagem 
# Aqui é return sem S
return contagem;

end $$

DELIMITER ;

# Verificar a execução da função
select contar_elementos()