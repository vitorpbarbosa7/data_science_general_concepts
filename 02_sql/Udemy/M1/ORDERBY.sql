-- ORDER BY 

/* SELECT column1, column2
FROM table
ORDER BY colunm1 asc/desc
*/

SELECT *
FROM Person.Person
ORDER BY LastName desc

SELECT *
FROM HumanResources.Employee
ORDER BY BirthDate

SELECT FirstName, LastName
FROM Person.Person
ORDER BY FirstName 

--DOIS ORDER BY? 

SELECT FirstName, LastName
FROM Person.Person
ORDER BY FirstName, LastName

--DESAFIO 1 : Obter ProductID dos 10 produtos mais caros cadastrados no sistema

SELECT TOP 10 ProductID, ListPrice
FROM Production.Product
ORDER BY ListPrice desc

--DESAFIO 2: 

SELECT Name, ProductNumber
FROM Production.Product
WHERE ProductID >= 1 AND ProductID <= 4

SELECT TOP 4 Name, ProductNumber
FROM Production.Product
ORDER BY ProductID asc




