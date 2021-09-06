-- BusinessEntityId, FirstName, LastName, EmailAdress

--Na tabela Person, a PK é a BusinessEntityID
SELECT TOP 10 * 
FROM Person.Person

--Na tabela EmailAdress a PK é o EmailAdressID e a FK é a BusinessEntityID
SELECT TOP 10 *
FROM Person.EmailAddress

SELECT a.BusinessEntityID, a.FirstName, a.LastName, b.EmailAddress
FROM Person.Person as a
INNER JOIN Person.EmailAddress as b on a.BusinessEntityID = b.BusinessEntityID

--Exercício
--Queremos os nomes dos produtos e as informações de suas subcategorias e o preço de cada um 

-- PK = ProductID; FK = ProductSubcategoryID
SELECT * 
FROM Production.Product

--PK = ProductSubCategoryID
SELECT *
FROM Production.ProductSubCategory

SELECT a.Name, a.ListPrice, b.*
FROM Production.Product as a
INNER JOIN Production.ProductSubcategory as b on a.ProductSubcategoryID = b.ProductSubCategoryID
ORDER BY a.ListPrice

--Juntar tudo:
SELECT *
FROM Person.BusinessEntityAddress

SELECT *
FROM Person.Address

--Para juntar tudo utiliza-se os alias para se referir à tabela inteira, não apenas a uma coluna
SELECT TOP 10 *
FROM Person.BusinessEntityAddress as BA
INNER JOIN Person.Address as PA ON BA.AddressID = PA.AddressID

SELECT *
FROM Person.BusinessEntityAddress as a
INNER JOIN Person.Address as b ON b.AddressID = a.AddressID

--Desafio:
-- BusinessEntityID, Name, PhoneNumberTypeId, PhoneNumber

SELECT TOP 10 *
FROM Person.Person

SELECT TOP 10 *
FROM Person.PhoneNumberType

SELECT TOP 10 *
FROM Person.PersonPhone

SELECT p.BusinessEntityID, p.FirstName, pp.PhoneNumberTypeId, pp.PhoneNumber
FROM Person.Person as p 
INNER JOIN Person.PersonPhone as pp ON p.BusinessEntityID = pp.BusinessEntityID

-- 2 Exercício:
SELECT TOP 10 *
FROM Person.StateProvince

SELECT TOP 10 * 
FROM Person.Address

-- AdressID, City, StateProvinceId, Nome do estado

SELECT AD.AddressId, AD.City, AD.StateProvinceID, SP.Name
FROM Person.Address as AD
INNER JOIN Person.StateProvince as SP ON AD.StateProvinceID = SP.StateProvinceID


