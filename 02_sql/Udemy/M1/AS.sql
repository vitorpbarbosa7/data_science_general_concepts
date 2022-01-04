--AS 

/* Para renomear uma coluna, uma agregação ou alguma outra coisa */

SELECT ListPrice as 'Preço Total'
FROM Production.Product

SELECT TOP 10 AVG(ListPrice) as 'Média'
FROM Production.Product

SELECT FirstName as 'Primeiro Nome', LastName as 'Último nome'
FROM Person.Person

SELECT ProductNumber as 'Número do produto'
FROM Production.Product 

SELECT UnitPrice as 'Preço unitário'
FROM Sales.SalesOrderDetail