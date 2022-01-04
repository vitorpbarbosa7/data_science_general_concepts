--SELECT * FROM person.Person

--SELECT *
--FROM person.Person 
--WHERE LastName = 'miller' AND FirstName = 'anna'

--Informações dos produtos cadastrados no Banco de Dados:
-- Dos vermelhos e azuis

--Filtro de cores
SELECT Name, Color 
FROM production.Product 
WHERE Color = 'Red' OR Color = 'Blue'

--Filtro de preço
SELECT Name, Color, ListPrice
FROM production.Product
WHERE ListPrice > 1500 AND ListPrice < 5000

--Nenhum produto vermelho:
SELECT * 
FROM production.Product
WHERE Color != 'Red'

--DESAFIO 1:
SELECT Name, Weight
FROM production.Product
WHERE Weight > 500 AND Weight < 700

--DESAFIO 2:
SELECT LoginID, MaritalStatus, SalariedFlag
FROM HumanResources.Employee
WHERE MaritalStatus = 'M' AND SalariedFlag = '1'

--DESAFIO 3:
SELECT * 
FROM Person.Person 
WHERE FIrstName = 'Peter' AND LastName = 'Krebs'

SELECT EmailAddress
FROM Person.EmailAddress
WHERE BusinessEntityID = '26'