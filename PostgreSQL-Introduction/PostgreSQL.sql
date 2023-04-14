CREATE DATABASE game_bar
USE DATABASE game_bar

CREATE TABLE employees (
	employee_id SERIAL PRIMARY KEY,
	first_name VARCHAR (10),
	last_name VARCHAR (5)
);

CREATE TABLE categories (
	category_id SERIAL PRIMARY KEY,
	category_name VARCHAR (50) NOT NULL,
);

CREATE CLASS products (
	product_id SERIAL PRIMARY KEY,
	product_name VARCHAR (50),
	category_id SERIAL
);


INSERT INTO employees
	VALUES (1, 'Gorge', 'R.'),
		   (2, 'Roburt', 'D.'),
		   (3, 'Josh', 'WR.');
		   
SELECT * FROM employees;

TRUNCATE TABLE employees;

DROP TABLE employees;

DROP DATABASE game_bar
