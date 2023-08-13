USE restaurant;

# 01. Departments Info
SELECT `department_id`, 
	COUNT(`id`) AS 'Number of employees'
    FROM `employees`
    GROUP BY `department_id`;


# 02. Average Salary
SELECT `department_id`,
	ROUND(AVG(`salary`), 2) AS 'Average Salary'
    FROM `employees`
    GROUP BY `department_id`
    ORDER BY `department_id`;


# 03. Minimum Salary
SELECT `department_id`,
	ROUND(MIN(`salary`), 2) AS 'Min Salary'
    FROM `employees`
    GROUP BY `department_id`
    HAVING `Min Salary` > 800;


# 04. Appetizers Count
   SELECT COUNT(`id`) FROM `products`
    WHERE `category_id` = 2 AND `price` > 8;


# 05. Menu Prices
SELECT `category_id`,
		ROUND(AVG(`price`), 2) AS 'Average Price',
        MIN(`price`) AS 'Cheapest Product',
        MAX(`price`) AS 'Most Expensive Product'
	FROM `products`
    GROUP BY `category_id`;
