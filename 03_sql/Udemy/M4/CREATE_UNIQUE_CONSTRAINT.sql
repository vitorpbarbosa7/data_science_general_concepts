-- UNIQUE CONSTRAINT

-- Um pouco diferente do Primary Key. 
-- Primary key pode ser definido apenas uma vez e o UNIQUE pode em várias colunas da mesma tabela

CREATE TABLE Onibus(
	ID int primary key, 
	Codigo varchar(7) NOT NULL UNIQUE
)

INSERT INTO Onibus(ID, Codigo)
VALUES
(1, '917H10')

INSERT INTO Onibus(ID, Codigo)
VALUES
(2, '478P10')

SELECT *
FROM Onibus

