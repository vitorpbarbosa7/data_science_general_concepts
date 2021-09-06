-- Criar tabela modalidade:
CREATE TABLE Modalidade (
	ModalidadeID INT Primary Key, 
	Nome varchar(150) NOT NULL
)

SELECT *
FROM Modalidade

--Onibus
CREATE TABLE Onibus (
	LinhaID char(6) Primary Key, 
	NomeIda varchar(150) NOT NULL, 
	NomeVolta varchar(150) NOT NULL, 
	Consorcio varchar(150) NOT NULL, 
	Viacao varchar(50) NOT NULL, 
	Kmida FLOAT NOT NULL, 
	Kmvolta FLOAT NOT NULL, 
	ModalidadeID INT Foreign Key REFERENCES Modalidade(ModalidadeID)
)

SELECT *
FROM Onibus

--Pontos
CREATE TABLE Pontos (
	PontoID INT Primary Key, 
	Lat DECIMAL NOT NULL, 
	Long DECIMAL NOT NULL 
)

CREATE TABLE Ponto_Linha (
	Ponto_LinhaID INT Primary Key, 
	NumeroLinhaID char(6) Foreign Key REFERENCES Onibus(LinhaID) NOT NULL,
	PontoId INT Foreign Key REFERENCES Pontos(PontoID)  NOT NULL
	)