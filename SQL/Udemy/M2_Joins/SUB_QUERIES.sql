SELECT * 
FROM Production.Product

-- Monte um relatório de todos os produtos cadastrados que apresentam preço de vendaa acima da média 

-- Qual a média?

SELECT AVG(ListPrice) as "Average"
FROM Production.Product

--Com a média, podemos:

SELECT *
FROM Production.Product
WHERE ListPrice > (SELECT AVG(ListPrice) as "Average"
					FROM Production.Product)

--Qual o nome dos funcionários que possuem o nome do cargo de 'Design Engineer'?

SELECT *
FROM HumanResources.Employee

SELECT *
FROM Person.Person

SELECT BusinessEntityID
FROM HumanResources.Employee
WHERE JobTitle = 'Design Engineer'

SELECT FirstName
FROM Person.Person
WHERE BusinessEntityID IN (SELECT BusinessEntityID
						FROM HumanResources.Employee
						WHERE JobTitle = 'Design Engineer')

-- Se quiser fazer com um JOIN:				

SELECT A.FirstName
FROM Person.Person A
INNER JOIN HumanResources.Employee B ON A.BusinessEntityID = B.BusinessEntityID -- Essa é a intersecção
WHERE B.JobTitle = 'Design Engineer'

--QUais são todos endereços que estão no estado de Alberta?

--Descobrir qual é o StateProvinceID de Aberta:
SELECT StateProvinceID
FROM Person.StateProvince
WHERE Name = 'Alberta'

SELECT *
FROM Person.Address
WHERE StateProvinceID IN (SELECT StateProvinceID
						FROM Person.StateProvince
						WHERE Name = 'Alberta')

--POR INNER JOIN						
SELECT *
FROM Person.Address A
INNER JOIN Person.StateProvince B ON A.StateProvinceID = B.StateProvinceID -- Éssa é a intersecção
WHERE B.Name = 'Alberta'