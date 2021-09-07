CREATE TABLE Youtube (
id int primary key, 
nome varchar(150) NOT NULL unique, 
categoria varchar(200) NOT NULL, 
dataCriacao datetime NOT NULL
)

SELECT * 
FROM Youtube

-- Adicionar uma coluna
ALTER TABLE youtube
add ativo bit 

SELECT *
FROM Youtube

-- Trocar o número de chars:
ALTER TABLE Youtube
ALTER COLUMN categoria varchar(300) NOT NULL

--Alterar o nome de uma coluna:
EXEC sp_Rename 'Youtube.dataCriacao', 'BirthDate', 'COLUMN'

--Alterar nome da tabela:
EXEC sp_Rename 'Youtube', 'Youtube2'

SELECT *
FROM Youtube

SELECT *
FROM Youtube2

/* Criar uma tabela nova com 3 colunas 
1) Alterar o tipo de uma coluna 
2) Renomear o nome de uma coluna
3) Renomear o nome da tabela que você criou 
*/

CREATE TABLE SSD (
  SSDID INT Primary Key, 
  Nome varchar(150) NOT NULL, 
  Marca varchar(150) NOT NULL, 
  Armazenamento INT NOT NULL, 
  Tipo varchar(20) NOT NULL, 
  ReadSpeed FLOAT NOT NULL, 
  WriteSpeed FLOAT NOT NULL 
)

SELECT *
FROM SSD

--1)
ALTER TABLE SSD
ALTER COLUMN Marca varchar(100) NOT NULL

--2)
EXEC sp_rename 'SSD.Tipo', 'Tecnologia', 'COLUMN'

SELECT *
FROM SSD

--3)
EXEC sp_rename 'SSD', 'SolidStateDrive'

SELECT *
FROM SSD

SELECT *
FROM SolidStateDrive

