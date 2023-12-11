ALTER 



-- SELECT * FROM products WHERE price != 600
-- SELECT username || ' ' || description as namedesv FROM products
-- SELECT * FROM products WHERE price between 500 and 1000
SELECT *FROM products
-- SELECT * FROM products WHERE username like 'iP%'
-- SELECT * FROM products WHERE username like '%d'

-- UPDATE products SET username = 'Iphone', description = 'gg hh ss'
-- WHERE id = 1

DELETE FROM products WHERE user_id = 1 


-- INSERT INTO products (description, username, price)
-- VALUES ('bla bla bla', 'Ipad', 900),
-- ('hjbbkbj', 'iWatch', 600),
-- ('shukhilk','iCar',100000)


--name - products
-- 3 cols:
-- id - serial 
-- name varchar 255 not null 
--price integer not null
-- desc varchar 1000

CREATE TABLE products(
	user_id serial PRIMARY KEY,
	username varchar (255) NOT NULL,
	price integer NOT NULL,
	description varchar(1000)
	)


-- CREATE TABLE accounts (

-- 	user_id serial PRIMARY KEY,
-- 	username varchar(50) UNIQUE NOT NULL,
-- 	password varchar (50) NOT NULL,
-- 	email varchar (255) UNIQUE NOT NULL,
-- 	create_on timestamp not null default now(),
-- 	last_login timestamp 

-- )
-- CREATE TABLE myuserstable(
-- 	id serial PRIMARY KEY,
-- 	email varchar(255) 	UNIQUE NOT NULL,
-- 	password varchar(1000),
-- 	created_date timestamp default now ()
-- )

--UNIQUE
--NOT NULL 
-- PRIMARY KEY  (unique for this column)
-- FOREIGN KEY 




