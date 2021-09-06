-- BETWEEN

SELECT * 
FROM Production.Product
WHERE ListPrice	BETWEEN 1000 AND 3000

-- NOT 

SELECT * 
FROM Production.Product
WHERE ListPrice	NOT BETWEEN 1000 AND 3000

SELECT *
FROM HumanResources.Employee
WHERE BirthDate BETWEEN '1971/01/01' AND '1981/01/01'
ORDER BY BirthDate desc

