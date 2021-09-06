create function `case_imposto` (salario dec(8,2))
returns dec(8,2)

begin

declare valor_imposto dec(8,2);

case 
when salario < 1903.98 then 
set valor_imposto = 0;

when salario > 1903.98 and salario < 2826.25 then 
set valor_imposto = salario * 0.075;

when salario > 2826.66 and salario < 3751.05 then 
set valor_imposto =  salario * 0.15;

when salario > 3751.05 and salario < 4664.68 then
set valor_imposto = salario * 0.225;

when salario > 4664.68 then 
set valor_imposto = salario * 0.275;

end case;

return valor_imposto;

end
