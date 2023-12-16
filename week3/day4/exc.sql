CREATE TABLE users (
	id serial PRIMARY KEY,
	username VARCHAR (50),
	email VARCHAR (255),
	age INTEGER
);

SELECT * FROM users