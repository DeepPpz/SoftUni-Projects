-- 1. Mountains and Peaks.
CREATE TABLE mountains (
	id SERIAL PRIMARY KEY,
	name VARCHAR(50)
	);

CREATE TABLE peaks (
	id SERIAL PRIMARY KEY,
	name VARCHAR(50),
	mountain_id INTEGER,
	CONSTRAINT fk_peaks_mountains
	FOREIGN KEY (mountain_id)
	REFERENCES mountains (id)
	);


-- 2. Trip Organization.
SELECT v.driver_id,
		v.vehicle_type,
		CONCAT(c.first_name, ' ', c.last_name) AS driver_name
	FROM vehicles v
	JOIN campers c 
		ON v.driver_id = c.id;


-- 3. SoftUni Hiking.
SELECT r.start_point,
		r.end_point,
		r.leader_id,
		CONCAT(c.first_name, ' ', c.last_name) AS leader_name
	FROM routes r 
	JOIN campers c 
		ON r.leader_id = c.id;


-- 4. Delete Mountains.
CREATE TABLE mountains (
	id SERIAL PRIMARY KEY,
	name VARCHAR(50)
	);

CREATE TABLE peaks (
	id SERIAL PRIMARY KEY,
	name VARCHAR(50),
	mountain_id INTEGER,
	CONSTRAINT fk_mountain_id
	FOREIGN KEY (mountain_id)
	REFERENCES mountains (id)
	ON DELETE CASCADE
	);


-- Project Management DB.
CREATE DATABASE project_management;

CREATE TABLE clients (
	id INTEGER PRIMARY KEY,
	name VARCHAR(100)
	);

CREATE TABLE employees (
	id INTEGER PRIMARY KEY,
	first_name VARCHAR(30),
	last_name VARCHAR(30),
	project_id INTEGER
	);

CREATE TABLE projects (
	id INTEGER PRIMARY KEY,
	client_id INTEGER,
	project_lead_id INTEGER,
	CONSTRAINT fk_projects_clients
	FOREIGN KEY (client_id)
	REFERENCES clients (id),
	CONSTRAINT fk_projects_employees
	FOREIGN KEY (project_lead_id)
	REFERENCES employees (id)
	);

ALTER TABLE employees
	ADD CONSTRAINT fk_employees_projects
	FOREIGN KEY (project_id)
	REFERENCES projects (id);

