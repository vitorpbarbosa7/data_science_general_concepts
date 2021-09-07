-- DESAFIO FUNDAMENTOS
/*
1 - Quantos produtos há cadastrados no sistema que custam mais que 1500 dolares?
*/

SELECT count(*)
FROM Production.Product
WHERE ListPrice > 1500

/* 
2 - Quantas pessoas iniciam o sobrenome com a letra P?
*/

SELECT count(*)
FROM Person.Person
WHERE LastName LIKE 'P%'

/*
3 - Quantas cidades únicas estão cadastradas nos clientes?
*/

SELECT count(DISTINCT City)
FROM Person.Address
--Há 575 cidades únicas

/*
4 - Quais são as cidades únicas que temos cadastrados em nosso sistema ? 
*/

SELECT DISTINCT City
FROM Person.Address

/*
5 - Quantos produtos vermelhos tem preço entre 500 e 1000 dólares
*/


SELECT count(*)
FROM Production.Product
WHERE Color IN ('Red') AND ListPrice BETWEEN 500 AND 1000

/*
6 - Quantos produtos cadastrados têm a palavra Road no nome deles?
*/

SELECT count(*)
FROM Production.Product
WHERE Name LIKE '%road%'