
CREATE TABLE actors1(
 actor_id SERIAL PRIMARY KEY,
 first_name VARCHAR (50) NOT NULL,
 last_name VARCHAR (100) NOT NULL,
 age DATE NOT NULL,
 number_oscars SMALLINT NOT NULL
)

INSERT INTO actors1 (first_name, last_name, age, number_oscars)
VALUES
    ('Meryl', 'Streep', '1949-06-22', 3),
	('Daniel', 'Day-Lewis', '1957-04-29', 3),
	('Jack', 'Nicholson', '1937-04-22', 3),
	('Matt', 'Damon', '1970-05-12', 2),
	('Tom', 'Hanks', '1956-07-09', 2)
	
SELECT * FROM actors1

--foreighn key
CREATE TABLE movies(
movie_id SERIAL,
movie_title VARCHAR (50) NOT NULL,
movie_story TEXT,
actor_playing_id INTEGER,
PRIMARY KEY (movie_id),
FOREIGN KEY (actor_playing_id) REFERENCES actors1 (actor_id)
);

INSERT INTO movies (movie_title, movie_story, actor_playing_id) VALUES
    ( 'Good Will Hunting', 
    'Written by Affleck and Damon, the film follows 20-year-old South Boston janitor Will Hunting',
    (SELECT actor_id from actors1 WHERE first_name='Matt' AND last_name='Damon')),
    ( 'Oceans Eleven', 
    'American heist film directed by Steven Soderbergh and written by Ted Griffin.', 
    (SELECT actor_id from actors1 WHERE first_name='Matt' AND last_name='Damon'));
select * from movies

SELECT actors1.first_name, actors1.last_name, movies.movie_title
FROM actors1
INNER JOIN movies
ON actors1.actor_id = movies.actor_playing_id;

SELECT actors1.first_name, actors1.last_name, movies.movie_title
FROM actors1
LEFT OUTER JOIN movies
ON actors1.actor_id = movies.actor_playing_id;

SELECT actors1.first_name, actors1.last_name, movies.movie_title
FROM actors1
RIGHT OUTER JOIN movies
ON actors1.actor_id = movies.actor_playing_id;

SELECT actors1.first_name, actors1.last_name, movies.movie_title
FROM actors1
FULL OUTER JOIN movies
ON actors1.actor_id = movies.actor_playing_id;