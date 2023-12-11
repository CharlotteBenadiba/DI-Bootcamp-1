--Questions 
--Q1
--This query fetches the count of records in FirstTab where the id is not NULL and not present in SecondTab where id is NULL.
--In subquary we have 0, then in quary it will be be not 3, but 0, because we cannot compair to 0.


--Q2
--This query counts the number of records in FirstTab where the id is not 5 and exists in SecondTab.
--In subquary we have 5, then in quary it will be not id 5, and not id NULL , so the outpur will be only 2 (6 and 7)

--Q3
--This query counts the number of records in FirstTab where the id does not exist in SecondTab.
--In subquary we will not have anything, because it's is impossible to compare something to NULL. Than is why the output will be 0.

--Q4
--This query counts the number of records in FirstTab where the id is not NULL and not present in SecondTab where id is not NULL.
--In subquary we have 5, then in quary it will be not id 5, and not id NULL , so the outpur will be only 2 (6 and 7)

-- CREATE TABLE FirstTab (
--      id integer, 
--      name VARCHAR(10)
-- )

-- INSERT INTO FirstTab VALUES
-- (5,'Pawan'),
-- (6,'Sharlee'),
-- (7,'Krish'),
-- (NULL,'Avtaar')

-- SELECT * FROM FirstTab

-- CREATE TABLE SecondTab (
--     id integer 
-- )

-- INSERT INTO SecondTab VALUES
-- (5),
-- (NULL)


-- SELECT * FROM SecondTab

--Q1
-- SELECT COUNT (*) FROM FirstTab AS ft WHERE ft.id NOT IN ( SELECT id FROM SecondTab WHERE id IS NULL )
--Output: 0 

--Q2
-- SELECT COUNT(*) FROM FirstTab AS ft WHERE ft.id NOT IN ( SELECT id FROM SecondTab WHERE id = 5 )
--Output: 2

--Q3
-- SELECT COUNT(*) FROM FirstTab AS ft WHERE ft.id NOT IN ( SELECT id FROM SecondTab )
--Output: 0 

--Q4
-- SELECT COUNT(*) FROM FirstTab AS ft WHERE ft.id NOT IN ( SELECT id FROM SecondTab WHERE id IS NOT NULL )
--Output: 2