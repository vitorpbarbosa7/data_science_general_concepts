-- Funções matemáticas

SELECT *
FROM Sales.SalesOrderDetail

SELECT UnitPrice + LineTotal
FROM Sales.SalesOrderDetail

SELECT UnitPrice / LineTotal
FROM Sales.SalesOrderDetail

SELECT Round(Linetotal, 2,2), LineTotal
FROM Sales.SalesOrderDetail

SELECT Round(SQRT(UnitPrice),2)
FROM Sales.SalesOrderDetail