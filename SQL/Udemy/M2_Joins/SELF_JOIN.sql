/* SELF JOIN

SELECT NOME_COLUNA
FROM TABELA A, TABELA B
WHERE CONDICAO

*/

SELECT *
FROM Customers

--Eu quero todos os clientes que moram na mesma região 
SELECT A.ContactName, A.Region, B.ContactName, B.Region
FROM Customers A, Customers B
WHERE A.Region = B.Region AND A.CustomerID <> B.CustomerID

--Qual o nome e data de contratação de todos os funcionários que foram contratados no mesmo ano? 
SELECT *
FROM Employees

SELECT A.FirstName, A.HireDate, B.FirstName, B.HireDate
FROM Employees A, Employees B
WHERE DATEPART(YEAR, A.HireDate) = DATEPART(YEAR, B.HireDate) AND A.EmployeeID <> B.EmployeeID

--Na tabela Order Details quais produtos têm o mesmo percentual de desconto?
SELECT *
FROM [Order Details]

SELECT DISTINCT A.ProductID, A.Discount, B.ProductID, B.Discount
FROM [Order Details] A, [Order Details] B
WHERE A.Discount = B.Discount


 