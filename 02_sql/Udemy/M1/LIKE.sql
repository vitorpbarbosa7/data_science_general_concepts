-- LIKE

SELECT *
FROM Person.Person
WHERE LastName LIKE 'Thi%'

SELECT *
FROM Person.CountryRegion
WHERE Name LIKE '%tri%'

SELECT *
FROM Person.Address
WHERE AddressLine1 LIKE '%Louis%'

SELECT *
FROM Person.Person
WHERE FirstName LIKE '%ro_' --Vai servir para o final do nome da pessoa né

SELECT *
FROM Sales.CreditCard 
WHERE CardType = 'SuperiorCard'

SELECT *
FROM Sales.Store
WHERE Name LIKE '%Bike%'