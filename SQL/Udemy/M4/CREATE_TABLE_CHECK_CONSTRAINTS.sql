-- Check Constraints

CREATE TABLE CarteiraMotorista(
	ID INT NOT NULL, 
	Nome varchar(255) NOT NULL, 
	Idade int CHECK (Idade >=18)
)

SELECT *
FROM CarteiraMotorista

INSERT INTO CarteiraMotorista(ID, Nome, Idade)
VALUES
(1, 'Elliot', 18)

---Criar duas tabelas novas e criar duas restrições para estas tabelas
-- duas restrições numéricas

CREATE TABLE VestibularIta(
	ID INT NOT NULL, 
	Nome varchar(255) NOT NULL, 
	CursoPretendido varchar(255) NOT NULL,
	Idade int check (Idade <= 23)
)

SELECT * 
FROM VestibularIta

INSERT INTO VestibularIta(ID, Nome, CursoPretendido, Idade)
VALUES
(1,'Fabricio', 'Engenharia da Computação',23) 

DROP TABLE RegistroFesta

CREATE TABLE RegistroFesta(
 ID INT NOT NULL, 
 Nome varchar(255) NOT NULL, 
 Sexo varchar(20) NOT NULL, 
 Idade int NOT NULL check (Idade >= 18) 
 )

SELECT * 
FROM RegistroFesta

INSERT INTO RegistroFesta(ID, Nome, Sexo, Idade)
VALUES
(1, 'Anderson', 'Masculino', 18)