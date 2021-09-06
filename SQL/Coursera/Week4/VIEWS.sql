--VIEWS

CREATE VIEW my_view 
AS
SELECT 
r.regiondescription, 
t.territorydescription, 
e.LastName, 
e.FirstName, 
e.Hiredate, 
e.Reportsto
FROM Region r
INNER JOIN Territories t on r.regionid = t.regionid
INNER JOIN Employeeterritories et on t.TerritoryID = et.TerritoryID
INNER JOIN Employees e on et.employeeid = e.EmployeeID

SELECT *
FROM my_view
DROP VIEW my_view