-- INSERT INTO

SELECT *
FROM Modalidade

INSERT INTO Modalidade(ModalidadeId, Nome)
VALUES
(2,'Metrô'),
(3,'Trem'),
(4,'Trolebus')

SELECT *
FROM Modalidade

--Copiando uma tabela:
SELECT * INTO TabelaNova from Modalidade

SELECT * 
FROM  TabelaNova

--Inserir 1 linha na nova tabela Onibus:
SELECT *
FROM Onibus

INSERT INTO Onibus(LinhaID, NomeIda, NomeVolta, Consorcio, Viacao, Kmida, Kmvolta, ModalidadeID)
VALUES
('477P10', 'Rio Pequeno', 'Ipiranga', 'Via Sudeste', 'Via Sudeste', 24, 22, 1),
('574J10', 'Terminal Vila Carrão', 'Conceicão', 'Via Sul', 'Via Sul', 20, 18, 1)

-- Inner Join com as tabelinhas que criei
SELECT A.*, B.*
FROM Onibus A
INNER JOIN Modalidade B ON A.ModalidadeID = B.ModalidadeID

--Copiar estes dados para outra tabela 
SELECT * INTO NewBusTable FROM Onibus

SELECT * FROM NewBusTable