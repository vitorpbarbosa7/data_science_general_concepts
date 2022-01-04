SELECT Birthdate, 
STRFTIME('%Y', Birthdate) as Year, 
STRFTIME('%m', Birthdate) as Month, 
STRFTIME('%d', Birthdate) as Day, 
DATE(('now') - Birthdate) as Age
FROM employees