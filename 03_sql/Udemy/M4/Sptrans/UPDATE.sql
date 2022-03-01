-- UPDATE

SELECT *
FROM Onibus

UPDATE Onibus
SET Kmvolta = 23 --Identifica coluna
WHERE LinhaID = '574J10' -- Identifica linha

--Alterar mais coisas
UPDATE Onibus 
SET Kmida = 25 
WHERE LinhaID = '477P10'
