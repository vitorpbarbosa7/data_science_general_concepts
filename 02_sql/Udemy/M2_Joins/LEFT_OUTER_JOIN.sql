/* 
LEFT OUTER JOIN:
Retornará todas PK de A, e as PK de A que estiverem em B, preenchendo com nulo os campos que não existirem em B da PK de A, mas não retornará PK de B. 

Pode ser abreviado apenas como LEFT JOIN 
*/

--Questão: Quais pessoas possuem um cartão de crédito?

--Ao rodar esta Query, na tabela Sales.PersonCreditCard, não é possível descobrir o nome das pessoas que possuem cartão de crédito
SELECT *
FROM Sales.PersonCreditCard

SELECT * 
FROM Person.Person

-- Retorna apenas a BusinessEntityID que existe em ambas as tabelas:
SELECT *
FROM Person.Person PP
INNER JOIN Sales.PersonCreditCard PC
ON PP.BusinessEntityID = PC.BusinessEntityID
-- COM INNER JOIN : 19118 linhas

-- Retorna todas as BusinessEntityID que existem na tabela A, mesmo que ela não exista na tabela B
SELECT *
FROM Person.Person PP
LEFT JOIN Sales.PersonCreditCard PC
ON PP.BusinessEntityID = PC.BusinessEntityID
ORDER BY PC.BusinessEntityID
-- COM LEFT JOIN : 19972 linhas

-- Mostrar pessoas sem cartão de crédito registrado:
SELECT *
FROM Person.Person PP
LEFT JOIN Sales.PersonCreditCard PC
ON PP.BusinessEntityID = PC.BusinessEntityID
WHERE PC.BusinessEntityID IS NULL
--Porque mostrará aquelas que existem na tabela A mas não existem na tabela B, 
--Se BusinessEntityID aparecer como NULL, significa que existe em A, mas não existe em B

-- 