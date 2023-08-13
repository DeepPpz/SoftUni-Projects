USE soft_uni;


# 01. Managers
SELECT e.`employee_id`,
		CONCAT(`first_name`, ' ', `last_name`) AS `full_name`,
        d.`department_id`,
        d.`name`
	FROM `employees` AS e
	RIGHT JOIN `departments` AS d
        ON d.`manager_id` =  e.`employee_id`
	ORDER BY e.`employee_id` LIMIT 5;


# 02. Towns and Addresses
SELECT t.`town_id`,
		t.`name` AS `town_name`,
        a.`address_text`
	FROM `towns` AS t
    JOIN `addresses` AS a
		ON a.`town_id` = t.`town_id`
	WHERE t.`name` IN ('San Francisco', 'Sofia', 'Carnation')
    ORDER BY `town_id`, `address_id`;


# 03. Employees Without Managers
SELECT `employee_id`,
		`first_name`,
        `last_name`,
        `department_id`,
        `salary`
	FROM `employees`
    WHERE `manager_id` IS NULL;


# 04. High Salary
SELECT COUNT(`employee_id`)
	FROM `employees`
    WHERE `salary` > (SELECT AVG(`salary`) 
				FROM `employees`);
