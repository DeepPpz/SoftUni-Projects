-- 01. Departments Info by ID.
SELECT department_id,
		COUNT(*) AS employee_count
	FROM employees
	GROUP BY department_id
	ORDER BY department_id;


-- 02. Departments Info by Salary.
SELECT department_id,
		COUNT(salary) AS employee_count
	FROM employees
	GROUP BY department_id
	ORDER BY department_id;


-- 03. Sum Salaries per Department.
SELECT department_id,
		SUM(salary) AS total_salaries
	FROM employees
	GROUP BY department_id 
	ORDER BY department_id;


-- 04. Maximum Salary.
SELECT department_id,
		MAX(salary) AS max_salary
	FROM employees
	GROUP BY department_id 
	ORDER BY department_id;


-- 05. Minimum Salary.
SELECT department_id,
		MIN(salary) AS min_salary
	FROM employees
	GROUP BY department_id 
	ORDER BY department_id;


-- 06. Average Salary.
SELECT department_id,
		AVG(salary) AS avg_salary
	FROM employees
	GROUP BY department_id 
	ORDER BY department_id;


-- 07. Filter Total Salaries.
SELECT department_id,
		SUM(salary) AS "Total Salary"
	FROM employees
	GROUP BY department_id
	HAVING SUM(salary) < 4200
	ORDER BY department_id;


-- 08. Department Names.
SELECT id,
		first_name,
		last_name,
		TO_CHAR(ROUND(salary, 3), '99999.00') AS salary,
		department_id,
		CASE
			WHEN department_id = 1 THEN 'Management'
			WHEN department_id = 2 THEN 'Kitchen Staff'
			WHEN department_id = 3 THEN 'Service Staff'
			ELSE 'Other'
		END AS department_name
	FROM employees;

