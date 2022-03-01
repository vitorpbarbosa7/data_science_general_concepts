/* COUNT

SELECT COUNT(*)
FROM TABLE

*/

SELECT *
FROM person.Person

SELECT count(*)
FROM person.Person

SELECT count(title)
FROM person.Person

SELECT count(DISTINCT title)
FROM person.Person

--DESAFIO 1 :
SELECT count(DISTINCT Name) 
FROM Production.Product

--Desafio 2 :
SELECT *
FROM Production.Product

SELECT count(DISTINCT Size)
FROM Production.Product