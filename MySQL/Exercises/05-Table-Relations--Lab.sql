USE camp;


# 01. Mountain and Peaks
CREATE TABLE `mountains` (
	`id` INT PRIMARY KEY AUTO_INCREMENT,
	`name` VARCHAR(255) NOT NULL
	);

CREATE TABLE `peaks` (
	`id` INT PRIMARY KEY AUTO_INCREMENT,
	`name` VARCHAR(255) NOT NULL,
	`mountain_id` INT NOT NULL,
	CONSTRAINT fk_peaks_mountains
	FOREIGN KEY (`mountain_id`)
	REFERENCES `mountains` (`id`)
	);


# 02. Trip Organization
SELECT `driver_id`, 
		`vehicle_type`,
		CONCAT(`first_name`, ' ', `last_name`) AS `driver_name`
	FROM `campers` AS c
	JOIN `vehicles` AS v
		ON v.`driver_id` = c.`id`;


# 03. SoftUni Hiking
SELECT `starting_point` AS `route_starting_point`,
		`end_point` AS `route_ending_point`,
		`leader_id`,
		CONCAT(`first_name`, ' ', `last_name`) AS `leader_name`
	FROM `campers` AS c
	JOIN `routes` AS r
		ON r.`leader_id` = c.`id`;


# 04. Delete Mountains
	# not in Judge
	DROP TABLE `peaks`;
	DROP TABLE `mountains`;

CREATE TABLE `mountains` (
	`id` INT PRIMARY KEY AUTO_INCREMENT,
	`name` VARCHAR(255) NOT NULL
	);

CREATE TABLE `peaks` (
	`id` INT PRIMARY KEY AUTO_INCREMENT,
	`name` VARCHAR(255) NOT NULL,
	`mountain_id` INT NOT NULL,
	CONSTRAINT fk_peaks_mountains
	FOREIGN KEY (`mountain_id`)
	REFERENCES `mountains` (`id`)
	ON DELETE CASCADE
	);


# 05. Project Management DB - not on Judge
CREATE TABLE `clients` (
	`id` INT PRIMARY KEY AUTO_INCREMENT,
	`client_name` VARCHAR(100)
	);

CREATE TABLE `projects` (
	`id` INT PRIMARY KEY AUTO_INCREMENT,
	`client_id` INT,
	`project_lead_id` INT
	);

CREATE TABLE `employees` (
	`id` INT PRIMARY KEY AUTO_INCREMENT,
	`first_name` VARCHAR(30),
	`last_name` VARCHAR(30),
	`project_id` INT,
	CONSTRAINT `fk_employees_projects`
	FOREIGN KEY (`project_id`)
	REFERENCES `projects` (`id`)
	);

ALTER TABLE `projects`
	ADD CONSTRAINT `fk_projects_clients`
	FOREIGN KEY (`client_id`)
	REFERENCES `clients` (`id`),
	ADD CONSTRAINT `fk_projects_employees`
	FOREIGN KEY (`project_lead_id`)
	REFERENCES `employees` (`id`);
