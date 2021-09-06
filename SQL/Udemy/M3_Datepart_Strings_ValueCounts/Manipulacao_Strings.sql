--Manipulação de String

SELECT *
FROM Person.Person

-- Juntar informações, concatenar informações 
-- CONCAT

SELECT CONCAT(FirstName, ' ',LastName) as 'Full Name'
FROM Person.Person

-- UPPER
SELECT UPPER(FirstName)
FROM Person.Person

-- LOWER 
SELECT LOWER(FirstName)
FROM Person.Person

-- SUBSTRING
SELECT SUBSTRING(FirstName,1,1), COUNT(*)
FROM Person.Person
GROUP BY SUBSTRING(FirstName,1,1)

-- REPLACE
SELECT *
FROM Production.Product

SELECT REPLACE(ProductNumber, '-', '#')
FROM Production.Product

SELECT REPLACE(Name, 'e', '3')
FROM Production.Product

