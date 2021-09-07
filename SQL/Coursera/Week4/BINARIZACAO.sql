SELECT trackid, name, bytes, 
CASE
WHEN bytes < 300000 THEN 'small'
WHEN bytes >= 300001 AND byest <= 500000 THEN 'medium'
WHEN bytes >= 500001 THEN 'large'
ELSE 'Other'
END bytescategory -- Nome da binarização, Nome da coluna
FROM tracks;