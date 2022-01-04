1 - 
SELECT Name 
FROM tracks
WHERE AlbumId IN
(SELECT AlbumId
FROM Albums
WHERE Title = 'Californication')
LIMIT 1 OFFSET 7]

2 - 
SELECT A.CustomerId, A.FirstName, A.LastName, A.City, A.Email, COUNT(B.InvoiceId)
FROM Customers as A
INNER JOIN Invoices as B ON A.CustomerId = B.CustomerId
GROUP BY A.CustomerId

4 - EMPLOYEEID, REPORTSTO 

SELECT *
FROM employees 
WHERE ReportsTo IN 
(SELECT EmployeeId
FROM employees
WHERE Title LIKE '%Manager%')
-- POR INNER JOIN :

SELECT A.LastName as "Manager", B.LastName as "Employee"
FROM employees A
INNER JOIN employees B ON B.ReportsTo = A.EmployeeId

7 - Diferença entre os dois?
SELECT A.BillingAddress, B.Address, COUNT
FROM invoices A
INNER JOIN customers B ON A.CustomerId = B.CustomerId

SELECT *
FROM 
(SELECT A.BillingAddress as "A", B.Address as "B"
FROM invoices A
INNER JOIN customers B ON A.CustomerId = B.CustomerId)
WHERE A <> B