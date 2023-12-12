CREATE TABLE products1(
	id serial PRIMARY KEY,
	name varchar (255) NOT NULL,
	price integer NOT NULL
	)
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

-- join 

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

CREATE TABLE products_desc (
	id serial PRIMARY KEY,
	description varchar (500),
	product_id integer NOT NULL,
	CONSTRAINT fk_products
		foreign key (product_id)
			references products(id)
	);

-- select * from products

-- INSERT INTO products_desc (description, product_id)

-- VALUES ('Amazing iPad', 1),
-- ('Best iWatch', 2),
-- ('Fastest car ever',3),
-- ('Great iPhone', 4)

--- DAY 3 ---

-- TABLE RELATIONS (1 TO 1 , )
-- ONE TO ONE CONNECTION (USER_ID CONNECT TO USER_ID UNIQUE)
create table users(
	user_id serial primary key,
	username varchar(50) unique not null,
	password varchar(1000)
	);
create table user_profile(
	profile_id serial primary key,
	user_id int unique not null REFERENCES users(user_id),
	first_name varchar(50)
	---
	);
--ONE TO MANY, BECAUSE USER_ID IS NOT UNIQUE
create table posts(
	post_id serial primary key,
	user_id int REFERENCES users(user_id),
	--.. title, bode, date
--MANY TO MANY (a lot of students to a lot of course)
create table students(
	student_id serial primary key,
	student_name varchar(100) not null
	--..last name, emal,
	)
INSERT INTO students (student_name)
	values ('John'),('Marry'),('Dan'),('Alla')
select * from students	
create table courses(
	course_id serial primary key,
	student_name varchar(100) not null
	--..
	)
	
	
INSERT INTO courses (courses_name)
	values ('Java'),('C++'),('React'),('NodeJS'),('Python'),('Sql')	
select * from courses		
create table student_course(
	id serial primary key,
	student_id int not null references students(student_id),
	course_id int not null references courses(course_id)
	)	
	
INSERT INTO student_course (student_id, course_id)
	values (1,4), (1,5),(1,6),
	(2,1), (2,2),
	(3,1), (3,2),(3,3),(3,4), (3,5),(3,6)
	
select* from 	student_course
	
select students.student_name, courses.courses_name
	from students
	inner join student_course
	on students.student_id = student_course.student_id
	inner join courses
	on courses.course_id = student_course.student_id
--FUNCTIONS
CREATE [OR REPLACE] FUNCTION function_name(param_list)
	returns return_type
	language plpgsql
as
$$
declare
	--variable names
begin 
	-- code / logic
--end	
--$$
	
create or replace function get_film_count(len_from int, len_to int)	
	returns int
	language plpgsql
as
$$
declare
	film_count integer
	film_count_b integer
begin 
	select count(1) into film_count
	from film
	where lenght between len_from and len_to;
	
	return film_count + film_count_b ;
	
end;	
$$	

select get_film_count (40,80)