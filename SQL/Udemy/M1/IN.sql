-- IN

SELECT *
FROM Production.Product
WHERE Color IN ('Black', 'Blue')

SELECT *
FROM Person.Person
WHERE BusinessEntityID IN (2,7,13)

SELECT *
FROM Person.Person
WHERE BusinessEntityID NOT IN (2,8,10,15)

SELECT *
FROM Person.Person
WHERE BusinessEntityID BETWEEN 2 AND 13