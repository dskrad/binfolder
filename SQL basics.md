-- Join
SELECT c.Name AS Country, c.Continent, ct.Name AS Capital
  FROM Country AS c
  JOIN City as ct
    ON ct.ID = c.Capital
  ORDER BY Country ;

-- Insert
INSERT INTO customer
  (name, city, state)
  VALUES (
    'John',
    'Springfield',
    'MA') ;

-- Where - Cities in Great Britain
SELECT * FROM City WHERE CountryCode = 'GBR' ;

-- Like - Cities starting with Z
SELECT * FROM City WHERE Name LIKE 'Z%' ;

-- IN & AND
SELECT * FROM City 
  WHERE CountryCode IN ('USA', 'CAN', 'GBR')
  AND Population > 1000000 ;

-- ORDER BY Name, Age
-- GROUP BY CountryCode

-- Update
UPDATE track SET title = "Swonderful"
  WHERE ID = 16 ;

-- Delete
DELETE FROM track WHERE ID = 70 ; 

-- String functions
CONCAT('s','1') ;
SUBSTR('abc',1,2) ;
RIGHT('this is the end',3) ; -- select rightmost 3 characters
LENGTH('four') ; --> 4
-- UPPER() and LOWER()