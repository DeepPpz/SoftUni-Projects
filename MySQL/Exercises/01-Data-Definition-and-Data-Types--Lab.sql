# 00. Create New Database
CREATE DATABASE `gamebar`;
USE `gamebar`;


# 01. Create Tables
CREATE TABLE `employees` (
	`id` INT PRIMARY KEY AUTO_INCREMENT,
    `first_name` VARCHAR(100) NOT NULL,
    `last_name` VARCHAR(100) NOT NULL
    );
    
CREATE TABLE `categories` (
	`id` INT PRIMARY KEY AUTO_INCREMENT,
    `name` VARCHAR(100) NOT NULL
    );
    
CREATE TABLE `products` (
	`id` INT PRIMARY KEY AUTO_INCREMENT,
    `name` VARCHAR(100) NOT NULL,
    `category_id` INT NOT NULL
    );


# 02. Insert Data in Tables
INSERT INTO `employees` (`first_name`, `last_name`)
	VALUES
		('Petar', 'Petrov'),
		('Ivan', 'Ivanov'),
		('Dimitar', 'Dimitrov');


# 03. Alter Table
ALTER TABLE `employees`
	ADD COLUMN `middle_name` VARCHAR(50);
    

# 04. Adding Constraints
ALTER TABLE `products`
	ADD CONSTRAINT `fk_products_categories`
		FOREIGN KEY `products` (`category_id`)
		REFERENCES `categories`(`id`);
    

# 05. Modifying Columns
ALTER TABLE `employees`
	MODIFY COLUMN `middle_name` VARCHAR(100);
