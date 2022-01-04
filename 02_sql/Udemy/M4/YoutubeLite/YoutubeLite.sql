

-- Criar tabela CANAL:
CREATE TABLE Canal (
	CanalId INT Primary Key,
	Nome varchar(150) NOT NULL,
	ContagemInscritos INT DEFAULT 0,
	DataCriacao DATETIME NOT NULL
);

SELECT *
FROM Canal

--Criar segunda tabela Video
CREATE TABLE Video (
	VideoId INT Primary Key, 
	Nome varchar(150) NOT NULL, 
	Visualizacoes INT DEFAULT 0,
	Likes INT DEFAULT 0, 
	Dislikes INT DEFAULT 0, 
	Duracao INT NOT NULL,
	CanalId INT Foreign Key REFERENCES Canal(CanalId)
)

SELECT *
FROM Vi