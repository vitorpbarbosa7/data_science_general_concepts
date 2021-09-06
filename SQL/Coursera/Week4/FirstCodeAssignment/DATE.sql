SELECT EmployeeID, 
FirstName || ' ' || Lastname as FullName, 
STRFTIME('%Y', DATE('now')) - STRFTIME('%Y', HireDate) as WorkingYears
FROM Employees