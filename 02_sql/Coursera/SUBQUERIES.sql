SELECT * FROM 
Sales.SalesOrderDetail

--Retorna apenas os produtos que possuem OrderQty >= 2
SELECT *
FROM Production.Product
WHERE ProductID IN 
(SELECT DISTINCT ProductID
FROM Sales.SalesOrderDetail
WHERE OrderQty >=3)


--INNER JOIN com uma SUBQUERY
SELECT DISTINCT PP.ProductID, PP.Name, SS.OrderQty
FROM Production.Product PP
INNER JOIN Sales.SalesOrderDetail SS 
ON PP.ProductID = SS.ProductID
WHERE PP.ProductID IN 
	(SELECT DISTINCT PP.ProductID
	FROM Sales.SalesOrderDetail
	WHERE SS.OrderQty >=3)
	
	ORDER BY PP.ProductID

--Subquery with COUNT
SELECT * 
FROM Production.Product

SELECT *
FROM Sales.SalesOrderDetail

SELECT Name, -- Da tabela Production.Product 
	(SELECT COUNT(*)
	FROM Sales.SalesOrderDetail
	WHERE Production.Product.ProductID = Sales.SalesOrderDetail.ProductID) AS Orders --Número de vezes que um produto aparece na tabela Sales.SalesOrderDetail
FROM Production.Product
ORDER BY Orders desc
	
