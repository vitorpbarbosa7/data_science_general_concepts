-- SUBSTRING
SELECT SUBSTRING(FirstName,1,1), COUNT(*)
FROM Person.Person
GROUP BY SUBSTRING(FirstName,1,1)