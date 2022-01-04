/* We can create binary classification like this. We could 
instead of using 'Calgary' used 0 and 1. 
It is like a OneHotEncoder */

-- Transform categorial values to binary 

CASE City
	WHEN 'Calgary' THEN 'Calgary'
	ELSE 'Other'
	END calgary -- Name of the calculation is calgary
FROM Employees
ORDER BY LastName, FirstName;