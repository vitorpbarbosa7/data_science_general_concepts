# Criação de função para retorno de valor 

# Função de cálculo de imposto 

# Imputar salário e retornar através da função o imposto sobre o salário

################## ATENÇÃO
# Precisa usar o :

set global log_bin_trust_function_creators = 1; 


# Fora de uma função e depois utilizar a janela de criação de função sem o DELIMITER porque ele já cria a sintaxe de definição do delimiter

create function `calcula_imposto` (salario dec(8,2))
returns dec(8,2)

# Nosso bloco que possui os comandos da função
begin

declare valor_imposto dec(8,2);

if salario < 1903.98 then 
set valor_imposto = 0;

elseif salario > 1903.99 and salario < 2826.65 then 
set valor_imposto = salario * 0.075;

elseif salario > 2826.66 and salario < 3751.05 then 
set valor_imposto = salario * 0.15;

elseif salario > 3751.05 and salario < 4664.68 then 
set valor_imposto = salario * 0.225;

else 
set valor_imposto = salario  * 0.275;

end if;

return valor_imposto;
end