

SELECT FirstName, LastName FROM
customers
WHERE CustomerId NOT IN 
/* 1) Primeiro SELECT que seleciona os CustomerId da tabela Invoice. 
Vamos utilizar esses CustomerId para ser o conjunto que não deve estar em customers */
(SELECT CustomerId
FROM invoices)

--NA REALIDADE PODERIA TER UTILIZADO UM FULL OUTER JOIN, PORQUE ELE NÃO IRIA PEGAR AQUELES QUE ESTÃO NA INTERSECÇÃO

-- Possível contar quantos há em cada um, quantos distintos há:
-- Ficar atento à ordem, pq estamos contando os distindos assim, ai ok 
SELECT COUNT(DISTINCT CustomerId)
FROM customers

SELECT COUNT(DISTINCT CustomerId)
FROM invoices
