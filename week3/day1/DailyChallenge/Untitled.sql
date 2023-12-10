-- CREATE TABLE actors(
--  actor_id SERIAL PRIMARY KEY,
--  first_name VARCHAR (50) NOT NULL,
--  last_name VARCHAR (100) NOT NULL,
--  age DATE NOT NULL,
--  number_oscars SMALLINT NOT NULL
-- )

-- INSERT INTO actors (first_name, last_name, age, number_oscars)
-- VALUES
--     ('Meryl', 'Streep', '1949-06-22', 3),
-- 	('Daniel', 'Day-Lewis', '1957-04-29', 3),
-- 	('Jack', 'Nicholson', '1937-04-22', 3),
-- 	('Matt', 'Damon', '1970-05-12', 2),
-- 	('Tom', 'Hanks', '1956-07-09', 2)
	
-- SELECT * FROM actors

-- ALTER TABLE actors RENAME COLUMN age TO birth_date;

-- SELECT * FROM actors WHERE first_name='Matt' AND last_name='Damon';
-- UPDATE actors SET first_name='Maty' WHERE first_name='Matt' AND last_name='Damon';
-- SELECT * FROM actors
-- UPDATE actors SET number_oscars=4 WHERE first_name='Tom' AND last_name='Hanks';

-- UPDATE actors SET birth_date='1970-01-01' WHERE first_name='Maty' AND last_name='Damon';

-- DELETE FROM actors WHERE actor_id=2
-- RETURNING actor_id, first_name, last_name, number_oscars;



-- --Daily Challenge 
-- SELECT COUNT (*) AS total_actors from actors

-- INSERT INTO actors (first_name, last_name)
-- VALUES ('John', '');
-- -- the outcome will be ERROR , because we put 'NOT NULL' definition in each parametr.
	
