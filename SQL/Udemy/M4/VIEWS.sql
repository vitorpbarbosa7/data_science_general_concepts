-- VIEWS

CREATE VIEW [Pessoas_ Simplificado] AS 
SELECT FirstName, MiddleName, LastName
FROM Person.Person
WHERE Title = 'Ms.'

SELECT * FROM [Pessoas_ Simplificado]
