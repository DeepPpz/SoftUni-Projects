-- 00. Create New Database.
CREATE DATABASE gamebar;


-- 01. Create Tables.
CREATE TABLE employees (
	id SERIAL PRIMARY KEY,
	first_name VARCHAR(30),
	last_name VARCHAR(50),
	hiring_date DATE DEFAULT '2023-01-01',
	salary DECIMAL(10, 2),
	devices_number INT
	);

CREATE TABLE departments (
	id SERIAL PRIMARY KEY,
	name VARCHAR(50),
	code CHAR(3),
	description TEXT
	);

CREATE TABLE issues (
	id SERIAL PRIMARY KEY,
	description VARCHAR(150),
	"date" DATE,
	"start" TIMESTAMP
	);


-- 02. Insert Data in Tables.
	-- * not in Judge
INSERT INTO employees (first_name, last_name)
	VALUES
		('Petar', 'Petrov'),
		('Ivan', 'Ivanov'),
		('Dimitar', 'Dimitrov');


-- 03. ALter Tables.
ALTER TABLE employees
	ADD COLUMN middle_name VARCHAR(50);


-- 04. Add Constraints.
ALTER TABLE employees
	ALTER COLUMN salary SET NOT NULL,
	ALTER COLUMN salary SET DEFAULT 0,
	ALTER COLUMN hiring_date SET NOT NULL;


-- 05. Modify Columns.
ALTER TABLE employees 
	ALTER COLUMN middle_name TYPE VARCHAR(100);


-- 06. Truncate Tables.
TRUNCATE TABLE issues;


-- 07. Drop Tables.
DROP TABLE departments;
