-- CREATE TABLE products1(
-- 	id serial PRIMARY KEY,
-- 	name varchar (255) NOT NULL,
-- 	price integer NOT NULL
-- 	)
-- ALTER TABLE products1 add column descroption varchar(1000);	
	
-- INSERT INTO products1 (name, price)
-- VALUES ('Ipad', 900),
-- ('iWatch', 600),
-- ('iCar',100000)

-- SELECT * FROM products1


	
-- --Aggregate func
-- --AVG
-- --COUNT
-- --MAX / MIN 
-- --SUM 

-- SELECT COUNT(1) FROM products1
-- SELECT sum(price) FROM products1
-- SELECT max(price) FROM products1
-- SELECT min(price) FROM products1
-- SELECT avg(price) FROM products1

-- select length (name),name, price from products1 where length(name) > 4

--join 

-- CREATE TABLE products2(
-- 	id serial PRIMARY KEY,
-- 	name varchar (255) NOT NULL,
-- 	price integer NOT NULL
-- 	)
-- INSERT INTO products2 (name, price)
-- VALUES ('Ipad', 900),
-- ('iWatch', 600),
-- ('iCar',100000),
-- ('iPhone',800)
-- SELECT * FROM products2

-- CREATE TABLE products_desc(
-- 	id serial PRIMARY KEY,
-- 	description varchar (500),
-- 	product_id integer NOT NULL
-- 	);
	
-- INSERT INTO products_desc (description, product_id)
-- VALUES ('Amazing iPad', 1),
-- ('Best iWatch', 2),
-- ('Fastest car ever',3),
-- ('Great iPhone', 4)
-- INSERT INTO products_desc (description, product_id)
-- VALUES ('Amazing iPad', 10),
-- ('Best iWatch', 11),
-- ('Fastest car ever',12),
-- ('Great iPhone', 13)

-- SELECT * FROM products_desc
-- SELECT * FROM products2
-- INNER JOIN products_desc
-- ON products2.id = products_desc.product_id

-- SELECT products2.id, products2.name, products2.price, products_desc.description FROM products2
-- INNER JOIN products_desc
-- ON products2.id = products_desc.product_id

-- SELECT products2.id, products2.name, products2.price, products_desc.description FROM products2
-- INNER JOIN products_desc
-- ON products2.id = products_desc.product_id

-- SELECT products2.id, products2.name, products2.price, products_desc.description FROM products2
-- left JOIN products_desc
-- ON products2.id = products_desc.product_id

-- SELECT products2.id, products2.name, products2.price, products_desc.description FROM products2
-- right JOIN products_desc
-- ON products2.id = products_desc.product_id

-- SELECT products2.id, products2.name, products2.price, products_desc.description FROM products2
-- full JOIN products_desc
-- ON products2.id = products_desc.product_id

-- SELECT products2.id, products2.name, products2.price, products_desc.description FROM products2, products_desc
-- INNER JOIN products_desc
-- ON products2.id = products_desc.product_id

-- select * from city
-- inner join country
-- on city.country_id =country

-- drop table products_desc;

-- CREATE TABLE products_desc (
-- 	id serial PRIMARY KEY,
-- 	description varchar (500),
-- 	product_id integer NOT NULL,
-- 	CONSTRAINT fk_products
-- 		foreign key (product_id)
-- 			references products(id)
-- 	);

-- select * from products

-- INSERT INTO products_desc (description, product_id)

-- VALUES ('Amazing iPad', 1),
-- ('Best iWatch', 2),
-- ('Fastest car ever',3),
-- ('Great iPhone', 4)


