-- UNION

--  COMBINAR DOIS 

--Combinar 2 ou mais resultados de 1 select em um resultado 

 /* 
 SELECT coluna1, coluna29
 FROM tabela1
 UNION 
 SELECT coluna1, coluna2
 FROM tabela2
 */

 SELECT ProductID, Name, ProductNumber 
 FROM Production.Product
 WHERE Name LIKE '%Chain%'
 UNION
 SELECT ProductID, Name, ProductNumber
 FROM Production.Product
 WHERE Name LIKE '%Decal%'

 -- De fato não consegui fazer funcionar de outra maneira
 SELECT ProductID, Name, ProductNumber
 FROM Production.Product
 WHERE NAME LIKE '%Chain%' OR '%Decal%'

 --Outro exemplo
 SELECT FirstName, Title
 FROM Person.Person
 WHERE Title = 'Mr.'
 UNION 
 SELECT FirstName, Title
 FROM Person.Person
 WHERE MiddleName = 'A'

 --Qualquer tabela no banco 