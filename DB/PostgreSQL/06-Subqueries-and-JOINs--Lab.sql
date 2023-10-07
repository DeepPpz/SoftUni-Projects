-- 01. Towns Addresses.
SELECT
	a.town_id,
	t.name,
	a.address_text
FROM
	addresses a
JOIN towns t 
	ON t.town_id = a.town_id
WHERE
	t.name IN ('San Francisco', 'Sofia', 'Carnation')
ORDER BY
	a.town_id,
	a.address_id;



-- 02. Managers.
SELECT
	d.manager_id,
	CONCAT(e.first_name, ' ', e.last_name) AS full_name,
	d.department_id,
	d.name AS department_name
FROM
	departments d
JOIN employees e 
	ON e.employee_id = d.manager_id
ORDER BY
	employee_id
LIMIT 5;



-- 03. Employees Projects.
SELECT
	e.employee_id,
	CONCAT(e.first_name, ' ', e.last_name) AS full_name,
	p.project_id,
	p.name as project_name
FROM
	employees e
JOIN employees_projects ep 
	ON ep.employee_id = e.employee_id
JOIN projects p 
	ON p.project_id = ep.project_id
WHERE
	ep.project_id = 1;



-- 04. Higher Salary.
SELECT 
	COUNT(*) as "count"
FROM 
	employees
WHERE 
	salary > (
		SELECT 
			AVG(salary)
		FROM 
			employees
	);

		
