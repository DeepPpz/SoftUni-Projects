CREATE DATABASE table_relations;
USE table_relations;


# 01. One-To-One Relationship
CREATE TABLE `passports` (
   `passport_id` INT PRIMARY KEY AUTO_INCREMENT,
   `passport_number` VARCHAR(50) UNIQUE
  	);
 
CREATE TABLE `people` (
   `person_id` INT PRIMARY KEY AUTO_INCREMENT,
   `first_name` VARCHAR(45),
   `salary` DECIMAL(9, 2),
   `passport_id` INT UNIQUE,
	CONSTRAINT fk_pe_pa
	FOREIGN KEY (`passport_id`)
	REFERENCES `passports`(`passport_id`)
	);
  
INSERT INTO `passports` (`passport_id`, `passport_number`) 
VALUES 
    (101, 'N34FG21B'), 
    (102, 'K65LO4R7'), 
    (103, 'ZE657QP2');
  
INSERT INTO `people` (`person_id`, `first_name`, `salary`, `passport_id`) 
VALUES 
    (1, 'Roberto', 43300.00, 102), 
    (2, 'Tom', 56100.00, 103), 
    (3, 'Yana', 60200.00, 101);


# 02. One-To-Many Relationship
CREATE TABLE `manufacturers` (
	`manufacturer_id` INT PRIMARY KEY AUTO_INCREMENT,
    `name` VARCHAR(50),
    `established_on` DATE
    );
    
CREATE TABLE `models` (
	`model_id` INT PRIMARY KEY AUTO_INCREMENT,
    `name` VARCHAR(50),
    `manufacturer_id` INT,
    CONSTRAINT `fk_models_manuf`
    FOREIGN KEY (`manufacturer_id`)
    REFERENCES `manufacturers` (`manufacturer_id`)
    );
    
INSERT INTO `manufacturers` (`manufacturer_id`, `name`, `established_on`)
	VALUES
		(1, 'BMW', '1916-03-01'),
        (2, 'Tesla', '2003-01-01'),
        (3, 'Lada', '1966-05-01');
        
INSERT INTO `models` (`model_id`, `name`, `manufacturer_id`)
	VALUES
		(101, 'X1', 1),
        (102, 'i6', 1),
        (103, 'Model S', 2),
        (104, 'Model X', 2),
        (105, 'Model 3', 2),
        (106, 'Nova', 3);


# 03. Many-To-Many Relationship
CREATE TABLE `students` (
	`student_id` INT PRIMARY KEY AUTO_INCREMENT,
    `name` VARCHAR(50)
    );
    
INSERT INTO `students` (`student_id`, `name`)
	VALUES
		(1, 'Mila'),
        (2, 'Toni'),
        (3, 'Ron');
    
CREATE TABLE `exams` (
	`exam_id` INT PRIMARY KEY AUTO_INCREMENT,
    `name` VARCHAR(50)
    );
    
INSERT INTO `exams` (`exam_id`, `name`)
	VALUES
		(101, 'Spring MVC'),
        (102, 'Neo4j'),
		(103, 'Oracle 11g');
    
CREATE TABLE `students_exams` (
	`student_id` INT,
    `exam_id` INT,
    CONSTRAINT `pk_students_exams`
    PRIMARY KEY (`student_id`, `exam_id`),
    CONSTRAINT `fk_stex_stud`
    FOREIGN KEY (`student_id`)
    REFERENCES `students` (`student_id`),
    CONSTRAINT `fk_stex_exams`
    FOREIGN KEY (`exam_id`)
    REFERENCES `exams` (`exam_id`)
    );
        
INSERT INTO `students_exams` (`student_id`, `exam_id`)
	VALUES
		(1, 101),
        (1, 102),
        (2, 101),
        (3, 103),
        (2, 102),
        (2, 103);


# 04. Self-Referencing
CREATE TABLE `teachers` (
	`teacher_id` INT PRIMARY KEY AUTO_INCREMENT,
    `name` VARCHAR(50),
    `manager_id` INT
    );
        
INSERT INTO `teachers` (`teacher_id`, `name`, `manager_id`)
	VALUES
		(101, 'John', NULL),
        (102, 'Maya', 106),
        (103, 'Silvia', 106),
        (104, 'Ted', 105),
        (105, 'Mark', 101),
        (106, 'Greta', 101);
        
ALTER TABLE `teachers`
	ADD CONSTRAINT `fk_manager_teacher`
	FOREIGN KEY (`manager_id`)
	REFERENCES `teachers` (`teacher_id`);


# 05. Online Store Database
	# not in Judge
	CREATE DATABASE `online_store`;
	USE `online_store`;

CREATE TABLE `item_types` (
	`item_type_id` INT PRIMARY KEY AUTO_INCREMENT,
    `name` VARCHAR(50)    
    );
    
CREATE TABLE `items` (
	`item_id` INT PRIMARY KEY AUTO_INCREMENT,
    `name` VARCHAR(50),
    `item_type_id` INT,
		CONSTRAINT `fk_items_itypes`
		FOREIGN KEY (`item_type_id`)
		REFERENCES `item_types` (`item_type_id`)
    );
    
CREATE TABLE `cities` (
	`city_id` INT PRIMARY KEY AUTO_INCREMENT,
    `name` VARCHAR(50)
    );
    
CREATE TABLE `customers` (
	`customer_id` INT PRIMARY KEY AUTO_INCREMENT,
    `name` VARCHAR(50),
    `birthday` DATE,
    `city_id` INT,
		CONSTRAINT `fk_customers_cities`
        FOREIGN KEY (`city_id`)
        REFERENCES `cities` (`city_id`)
    );
    
CREATE TABLE `orders` (
	`order_id` INT PRIMARY KEY AUTO_INCREMENT,
    `customer_id` INT,
		CONSTRAINT `fk_orders_customers`
        FOREIGN KEY (`customer_id`)
        REFERENCES `customers` (`customer_id`)
    );
    
CREATE TABLE `order_items` (
	`order_id` INT,
    `item_id` INT,
		CONSTRAINT `pk_order_items`
        PRIMARY KEY (`order_id`, `item_id`),
		CONSTRAINT `fk_orit_orders`
        FOREIGN KEY (`order_id`)
        REFERENCES `orders` (`order_id`),
        CONSTRAINT `fk_orit_items`
        FOREIGN KEY (`item_id`)
        REFERENCES `items` (`item_id`)
    );


# 06. University Database
	#not in Judge
	CREATE DATABASE `university`;
	USE `university`;

CREATE TABLE `majors` (
	`major_id` INT PRIMARY KEY AUTO_INCREMENT,
    `name` VARCHAR(50)
    );
    
CREATE TABLE `students` (
	`student_id` INT PRIMARY KEY AUTO_INCREMENT,
    `student_number` VARCHAR(12),
    `student_name` VARCHAR(50),
    `major_id` INT,
		CONSTRAINT fk_students_majors
        FOREIGN KEY (`major_id`)
        REFERENCES `majors` (`major_id`)
    );
    
CREATE TABLE `payments` (
	`payment_id` INT PRIMARY KEY AUTO_INCREMENT,
    `payment_date` DATE,
    `payment_amount` DECIMAL(8,2),
    `student_id` INT,
		CONSTRAINT 	`fk_payments_students`
        FOREIGN KEY (`student_id`)
        REFERENCES `students` (`student_id`)
    );
    
CREATE TABLE `subjects` (
	`subject_id` INT PRIMARY KEY AUTO_INCREMENT,
    `subject_name` VARCHAR(50)
    );
    
CREATE TABLE `agenda` (
	`student_id` INT,
    `subject_id` INT,
		PRIMARY KEY (`student_id`, `subject_id`),
        CONSTRAINT `fk_agenda_students`
        FOREIGN KEY (`student_id`)
        REFERENCES `students` (`student_id`),
        CONSTRAINT `fk_agenda_subjects`
        FOREIGN KEY (`subject_id`)
        REFERENCES `subjects` (`subject_id`)
    );


USE soft_uni;

# 07. SoftUni Design - not on Judge.
	# Just look at E/R Diagram of soft_uni database.


USE geography;

# 08. Geography Design - not on Judge.
	# Just look at E/R Diagram of geography database.


# 09. Peaks in Rila
SELECT `mountain_range`,
		`peak_name`,
        `elevation`
	FROM `mountains`, `peaks`
    WHERE `peaks`.`mountain_id` = `mountains`.`id`
		AND `mountain_range` = 'Rila'
	ORDER BY `elevation` DESC;
