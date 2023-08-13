# 00. Create Database
CREATE DATABASE `minions`;
USE `minions`;


# 01. Create Tables
CREATE TABLE `minions` (
	`id` INT PRIMARY KEY AUTO_INCREMENT,
    `name` VARCHAR(255) NOT NULL,
    `age` INT
    );
    
CREATE TABLE `towns` (
	`town_id` INT PRIMARY KEY AUTO_INCREMENT,
    `name` VARCHAR(255) NOT NULL
    );


# 02. Alter Minions Table
	#not in Judge:
    ALTER TABLE `towns` 
		RENAME COLUMN `town_id` TO `id`;
    
ALTER TABLE `minions`
	ADD COLUMN `town_id` INT NOT NULL,
    ADD CONSTRAINT `fk_minions_towns`
		FOREIGN KEY (`town_id`)
        REFERENCES `towns` (`id`);


# 03. Insert Records in Both Tables
INSERT INTO `towns` (`id`, `name`)
	VALUES
		(1, 'Sofia'),
        (2, 'Plovdiv'),
        (3, 'Varna');

INSERT INTO `minions` (`id`, `name`, `age`, `town_id`)
	VALUES
		(1, 'Kevin', 22, 1),
        (2, 'Bob', 15, 3),
        (3, 'Steward', NULL, 2);


# 04. Truncate Table Minions
TRUNCATE TABLE `minions`;


# 05. Drop All Tables
DROP TABLE `minions`;

DROP TABLE `towns`;


# 06. Create Table People
CREATE TABLE `people` (
	`id` INT PRIMARY KEY AUTO_INCREMENT,
    `name` VARCHAR(200) NOT NULL,
    `picture` BLOB,
    `height` DOUBLE(5,2),
    `weight` DOUBLE(5,2),
    `gender` ENUM('M', 'F') NOT NULL,
    `birthdate` DATE NOT NULL,
    `biography` TEXT
    );

INSERT INTO `people` (`name`, `gender`, `birthdate`)
	VALUES
		('Petko', 'M', '2000-06-07'),
        ('Maria', 'F', '1978-08-17'),
        ('Georgi', 'M', '1994-01-27'),
        ('Ivan', 'M', '1960-03-03'),
        ('Borislava', 'F', '2001-12-01');
        

# 07. Create Table Users
CREATE TABLE `users` (
	`id` BIGINT AUTO_INCREMENT,
    `username` VARCHAR(30) NOT NULL,
    `password` VARCHAR(26) NOT NULL,
    `profile_picture` BLOB,
    `last_login_time` DATETIME,
    `is_deleted` BOOLEAN,
		CONSTRAINT `pk_users`
			PRIMARY KEY (`id`)
    );
    
INSERT INTO `users` (`username`, `password`)
	VALUES
		('gosho00', 'ghtaj355'),
        ('sladka06', 'sladka06'),
        ('dumbsh', 'rhsysfvn1'),
        ('slayer', 'hottopic'),
        ('theboxer', 'brandon');


# 08. Change Primary Key
ALTER TABLE `users`
	DROP PRIMARY KEY,
    ADD PRIMARY KEY `pk_users` (`id`, `username`);
    

# 9. Set Default Value of a Field
ALTER TABLE `users`
	MODIFY COLUMN `last_login_time` DATETIME NULL DEFAULT NOW();
    

# 10. Set Unique Field
ALTER TABLE `users`
	DROP PRIMARY KEY,
    ADD PRIMARY KEY `pk_users` (`id`),
    MODIFY COLUMN `username` VARCHAR(30) UNIQUE;


# 11. Movies Database
	#not in Judge:
		CREATE DATABASE `movies`;
		USE `movies`;

CREATE TABLE `directors` (
	`id` INT PRIMARY KEY AUTO_INCREMENT,
    `director_name` VARCHAR(100) NOT NULL,
    `notes` TEXT
    );

CREATE TABLE `genres` (
	`id` INT PRIMARY KEY AUTO_INCREMENT,
    `genre_name` VARCHAR(100) NOT NULL,
    `notes` TEXT
    );

CREATE TABLE `categories` (
	`id` INT PRIMARY KEY AUTO_INCREMENT,
    `category_name` VARCHAR(100) NOT NULL,
    `notes` TEXT
    );

CREATE TABLE `movies` (
	`id` INT PRIMARY KEY AUTO_INCREMENT,
    `title` VARCHAR(255) NOT NULL,
    `director_id` INT,
    `copyright_year` YEAR,
    `length` INT,
    `genre_id` INT,
    `category_id` INT,
    `rating` INT,
    `notes` TEXT
    );

INSERT INTO `directors` (`id`, `director_name`)
	VALUES
		(1, 'Frank Darabont'),
        (2, 'Christopher Nolan'),
        (3, 'Quentin Tarantino'),
        (4, 'Robert Zemeckis'),
        (5, 'Alfred Hitchcock');

INSERT INTO `genres` (`id`, `genre_name`)
	VALUES
		(1, 'Drama'),
        (2, 'Action'),
        (3, 'Crime'),
        (4, 'Sci-Fi'),
        (5, 'Horror');

INSERT INTO `categories` (`id`, `category_name`)
	VALUES
		(1, 'G'),
        (2, 'PG'),
        (3, 'PG-13'),
        (4, 'R'),
        (5, 'NC-17');
        
INSERT INTO `movies` (`id`, `title`, `director_id`, `copyright_year`, `genre_id`, `category_id`)
	VALUES
		(1, 'The Shawshank Redemption', 1, 1994, 1, 4),
        (2, 'The Dark Knight', 2, 2008, 2, 3),
        (3, 'Pulp Fiction', 3, 1994, 3, 4),
        (4, 'Back to the Future', 4, 1985, 4, 2),
        (5, 'Psycho', 5, 1960, 5, 4);


# 12. Car Rental Database
	#not in Judge
		CREATE DATABASE `car_rental`;
		USE `car_rental`;

CREATE TABLE `categories` (
	`id` INT PRIMARY KEY AUTO_INCREMENT,
    `category` VARCHAR(100) NOT NULL,
    `daily_rate` INT,
    `weekly_rate` INT,
    `monthly_rate` INT,
    `weekend_rate` INT
    );

CREATE TABLE `cars` (
	`id` INT PRIMARY KEY AUTO_INCREMENT,
    `plate_number` VARCHAR(10) NOT NULL,
    `make` VARCHAR(100),
    `model` VARCHAR(100),
    `car_year` YEAR,
    `category_id` INT,
    `doors` INT,
    `picture` BLOB,
    `car_condition` VARCHAR(10),
    `available` BOOLEAN
    );

CREATE TABLE `employees` (
	`id` INT PRIMARY KEY AUTO_INCREMENT,
    `first_name` VARCHAR(100) NOT NULL,
    `last_name` VARCHAR(100),
    `title` VARCHAR(100),
    `notes` TEXT
    );
    
CREATE TABLE `customers` (
	`id` INT PRIMARY KEY AUTO_INCREMENT,
    `driver_licence_number` INT,
    `full_name` VARCHAR(100),
    `address` VARCHAR(100),
    `city` VARCHAR(50),
    `zip_code` VARCHAR(10),
    `notes` TEXT
    );

CREATE TABLE `rental_orders` (
	`id` INT PRIMARY KEY AUTO_INCREMENT,
    `employee_id` INT,
    `customer_id` INT,
    `car_id` INT,
    `car_condition` VARCHAR(100),
    `tank_level` VARCHAR(100),
    `kilometrage_start` INT,
    `kilometrage_end` INT,
    `total_kilometrage` INT,
    `start_date` DATE,
    `end_date` DATE,
    `total_days` INT,
    `rate_applied` INT,
    `tax_rate` INT,
    `order_status` VARCHAR(100),
    `notes` TEXT
    );

INSERT INTO `categories` (`id`, `category`)
	VALUES
		(1, 'Category 1'),
        (2, 'Category 2'),
        (3, 'Category 3');

INSERT INTO `cars` (`id`, `plate_number`, `make`, `model`)
	VALUES
		(1, '634857', 'Opel', 'Astra'),
        (2, '249337', 'Volkswagen', 'Golf'),
        (3, '559977', 'BMW', 'E60');
        
INSERT INTO `employees` (`id`, `first_name`)
	VALUES
		(1, 'Georgi'),
        (2, 'Maria'),
        (3, 'Ivan');

INSERT INTO `customers` (`id`, `driver_licence_number`, `full_name`)
	VALUES
		(1, '379528476', 'Peter'),
        (2, '934678265', 'Veronika'),
        (3, '246735876', 'Roza');
        
INSERT INTO `rental_orders` (`id`, `employee_id`, `customer_id`, `car_id`)
	VALUES
		(1, 1, 1, 1),
        (2, 2, 2, 2),
        (3, 3, 3, 3);


# 13. Basic Insert
	# not in Judge (all creatings)
	CREATE DATABASE `soft_uni`;
	USE `soft_uni`;
    
    CREATE TABLE `towns` (
		`id` INT PRIMARY KEY AUTO_INCREMENT,
        `name` VARCHAR(50) NOT NULL
        );
        
    CREATE TABLE `addresses` (
		`id` INT PRIMARY KEY AUTO_INCREMENT,
        `address_text` VARCHAR(100),
        `town_id` INT,
			CONSTRAINT `fk_addresses_towns`
				FOREIGN KEY (`town_id`)
                REFERENCES `towns` (`id`)
        );
        
    CREATE TABLE `departments` (
		`id` INT PRIMARY KEY AUTO_INCREMENT,
        `name` VARCHAR(100) NOT NULL
        );
        
    CREATE TABLE `employees` (
		`id` INT PRIMARY KEY AUTO_INCREMENT,
        `first_name` VARCHAR(50),
        `middle_name` VARCHAR(50),
        `last_name` VARCHAR(50),
        `job_title` VARCHAR(50),
        `department_id` INT,
        `hire_date` DATE,
        `salary` DECIMAL(10,2),
        `address_id` INT
			);

	ALTER TABLE `employees`
		ADD CONSTRAINT `fk_employees_departments`
			FOREIGN KEY (`department_id`)
            REFERENCES `departments` (`id`),
		ADD CONSTRAINT `fk_employees_address_id`
			FOREIGN KEY (`address_id`)
            REFERENCES `addresses` (`id`);

INSERT INTO `towns` (`id`, `name`)
	VALUES
		(1, 'Sofia'),
        (2, 'Plovdiv'),
        (3, 'Varna'),
        (4, 'Burgas');

INSERT INTO `departments` (`id`, `name`)
	VALUES
		(1, 'Engineering'),
        (2, 'Sales'),
        (3, 'Marketing'),
        (4, 'Software Development'),
        (5, 'Quality Assurance');

INSERT INTO `employees` (`first_name`, `middle_name`, `last_name`, `job_title`, `department_id`, `hire_date`, `salary`)
	VALUES
		('Ivan', 'Ivanov', 'Ivanov', '.NET Developer', 4, '2013-02-01', '3500.00'),
		('Petar', 'Petrov', 'Petrov', 'Senior Engineer', 1, '2004-03-02', '4000.00'),
		('Maria', 'Petrova', 'Ivanova', 'Intern', 5, '2016-08-28', '525.25'),
		('Georgi', 'Terziev', 'Ivanov', 'CEO', 2, '2007-12-09', '3000.00'),
		('Peter', 'Pan', 'Pan', 'Intern', 3, '2016-08-28', '599.88');


# 14. Basic Select All Fields
SELECT * FROM `towns`;

SELECT * FROM `departments`;

SELECT * FROM `employees`;


# 15. Basic Select All Fields and Order Them
SELECT * FROM `towns`
	ORDER BY `name`;

SELECT * FROM `departments`
	ORDER BY `name` ASC;

SELECT * FROM `employees`
	ORDER BY `salary` DESC;


# 16. Basic Select Some Fields
SELECT `name` FROM `towns`
	ORDER BY `name`;

SELECT `name` FROM `departments`
	ORDER BY `name` ASC;

SELECT `first_name`, `last_name`,
		`job_title`, `salary`
	FROM `employees`
	ORDER BY `salary` DESC;


# 17. Increase Employees Salary
UPDATE `employees`
	SET `salary` = `salary` * 1.10;

SELECT `salary` FROM `employees`;
