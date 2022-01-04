SELECT E.*, F.UnitPrice
FROM

/*Segundo SELECT para INNER JOIN e trazer o TrackId que vai permitir ir até a 
tabela invoice_items*/
(SELECT C.AlbumId, C.Title, D.TrackId
FROM
/* PRIMEIRO SELECT entre artists e albums para trazer o nome dos albums, de 
acordo com o ArtistId do Name 'Audioslave' */
(SELECT A.Name, B.AlbumId, B.Title
FROM artists A
INNER JOIN albums B ON A.ArtistId = B.ArtistId
WHERE A.Name = 'Audioslave') as C 

INNER JOIN tracks as D ON C.AlbumId = D.AlbumId) as E

INNER JOIN invoice_items as F ON E.TrackId = F.TrackId


-- PREÇO TOTAL DOS ALBUMS DE ACORDO COM OS PREÇOS UNITÁRIOS
--Último SELECT que permite finalmente trazer a tabela invoice_items com os devidos UnitPrice
SELECT E.*, SUM(F.UnitPrice)
FROM

/*Segundo SELECT para INNER JOIN e trazer o TrackId que vai permitir ir até a 
tabela invoice_items*/
(SELECT C.AlbumId, C.Title, D.TrackId
FROM
/* PRIMEIRO SELECT entre artists e albums para trazer o nome dos albums, de 
acordo com o ArtistId do Name 'Audioslave' */
(SELECT A.Name, B.AlbumId, B.Title
FROM artists A
INNER JOIN albums B ON A.ArtistId = B.ArtistId
WHERE A.Name = 'Audioslave') as C 

INNER JOIN tracks as D ON C.AlbumId = D.AlbumId) as E

INNER JOIN invoice_items as F ON E.TrackId = F.TrackId

GROUP BY Title