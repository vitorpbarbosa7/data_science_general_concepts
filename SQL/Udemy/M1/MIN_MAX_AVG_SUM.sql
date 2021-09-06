-- MIN MAX SUM AVG

SELECT TOP 10 *
from Sales.SalesOrderDetail

-- MAX

SELECT MAX(UnitPrice) AS "Maximum"
FROM Sales.SalesOrderDetail

-- MIN

SELECT MIN(UnitPrice) AS "Minimum"
FROM Sales.SalesOrderDetail

-- AVG

SELECT AVG(UnitPrice) AS "Average"
FROM Sales.SalesOrderDetail

-- SUM 

SELECT SUM(UnitPrice) AS "Sum"
FROM Sales.SalesOrderDetail

SELECT SUM(LineTotal) AS "Sum"
FROM Sales.SalesOrderDetail