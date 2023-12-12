CREATE TABLE colors (
    color_id INT PRIMARY KEY,
    color_name VARCHAR(50)
);

CREATE TABLE cars(
	car_id INT PRIMARY KEY,
    car_name VARCHAR(50),
	car_color INTEGER REFERENCES colors (color_id) ON DELETE cascade

);

INSERT INTO colors (color_id, color_name) VALUES
(1, 'Blue'),
(2, 'Yellow'),
(3, 'Pink');

INSERT INTO cars (car_id, car_name, car_color) VALUES
(1, 'Mazda', 1),
(2, 'bmv', 2), 
(3, 'Bugatti', 3)

DELETE FROM colors

SELECT cars.car_id, cars.car_name, colors.color_name as color
FROM cars
INNER JOIN colors
ON cars.car_id = colors.color_id;

DROP TABLE cars;
DELETE FROM colors where color_name = 'yellow';
SELECT  * FROM cars
SELECT  * FROM colors

DELETE FROM colors where color_name = 'Pink';

SELECT cars.car_id, cars.car_name, colors.color_name as color
FROM colors
INNER JOIN cars
ON colors.color_id = cars.car_id;