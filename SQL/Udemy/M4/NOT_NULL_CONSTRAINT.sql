-- NOT NULL CONSTRAINT

DROP TABLE Notebook

CREATE TABLE Notebook(
	ID INT NOT NULL, 
	Nome varchar(255) NOT NULL, 
	Modelo varchar(100) NOT NULL, 
	Preco FLOAT NOT NULL
)

INSERT INTO Notebook(ID, Nome, Modelo, Preco)
VALUES
(1,'Dell','xps',15.500)

SELECT *
FROM Notebook


--Criando tabela que permite valore nulos

CREATE TABLE Show(
	ID INT primary key,
	Artista varchar(255) NOT NULL,
	Localizacao varchar(255)
	)

INSERT INTO Show(ID, Artista)
VALUES
(1,'Legião Urbana')

-- Não deixa porque Artista é obrigatório (NOT NULL)
INSERT INTO Show(ID, Localizacao)
VALUES
(2, 'Santo Rock Bar')

CREATE TABLE 