--- 01. COUNT of Records.
SELECT
	COUNT(*)
FROM
	wizard_deposits;



-- 02. Total Deposit Amount.
SELECT
	SUM(deposit_amount)
FROM
	wizard_deposits;



-- 03. AVG Magic Wand Size.
SELECT
	ROUND(AVG(magic_wand_size), 3)
FROM
	wizard_deposits;



-- 04. MIN Deposit Charge.
SELECT
	MIN(deposit_charge)
FROM
	wizard_deposits;



-- 05. MAX Age.
SELECT
	MAX(age)
FROM
	wizard_deposits;



-- 06. GROUP BY Deposit Interest.
SELECT
	deposit_group,
	SUM(deposit_interest) AS "Deposit Interest"
FROM
	wizard_deposits
GROUP BY
	deposit_group
ORDER BY
	"Deposit Interest" DESC;



-- 07. LIMIT the Magic Wand Creator.
SELECT
	magic_wand_creator,
	MIN(magic_wand_size) AS "Minimum Wand Size"
FROM
	wizard_deposits
GROUP BY
	magic_wand_creator
ORDER BY
	"Minimum Wand Size" ASC
LIMIT 5;



-- 08. Bank Profitability.
SELECT
	deposit_group,
	is_deposit_expired,
	FLOOR(AVG(deposit_interest)) AS "Deposit Interest"
FROM
	wizard_deposits
WHERE
	deposit_start_date > '1985-01-01'
GROUP BY
	deposit_group,
	is_deposit_expired
ORDER BY
	deposit_group DESC,
	is_deposit_expired ASC;



-- 09. Notes with Dumbledore.
SELECT
	last_name,
	COUNT(*) AS "Notes with Dumbledore"
FROM
	wizard_deposits
WHERE
	notes LIKE '%Dumbledore%'
GROUP BY
	last_name;



-- 10. Wizard View.
CREATE VIEW view_wizard_deposits_with_expiration_date_before_1983_08_17 AS
	SELECT
		CONCAT(first_name, ' ', last_name) AS "Wizard Name",
		deposit_start_date AS "Start Date",
		deposit_expiration_date AS "Expiration Date",
		deposit_amount AS "Amount"
	FROM
		wizard_deposits
	WHERE
		deposit_expiration_date <= '1983-08-17'
	GROUP BY
		"Wizard Name",
		"Start Date",
		"Expiration Date",
		"Amount"
	ORDER BY
		"Expiration Date" ASC;



-- 11. Filter Max Deposit.
SELECT
	magic_wand_creator,
	MAX(deposit_amount) AS "Max Deposit Amount"
FROM
	wizard_deposits
GROUP BY
	magic_wand_creator
HAVING
	MAX(deposit_amount) NOT BETWEEN 20000 AND 40000
ORDER BY
	"Max Deposit Amount" DESC
LIMIT 3;



-- 12. Age Group.
SELECT 
	CASE
		WHEN age BETWEEN 0 AND 10 THEN '[0-10]'
		WHEN age BETWEEN 11 AND 20 THEN '[11-20]'
		WHEN age BETWEEN 21 AND 30 THEN '[21-30]'
		WHEN age BETWEEN 31 AND 40 THEN '[31-40]'
		WHEN age BETWEEN 41 AND 50 THEN '[41-50]'
		WHEN age BETWEEN 51 AND 60 THEN '[51-60]'
		ELSE '[61+]'
	END AS "Age Group",
	COUNT(*) AS "count"
FROM
	wizard_deposits
GROUP BY
	"Age Group"
ORDER BY
	"Age Group" ASC;



-- 13. SUM the Employees.
SELECT 
	COUNT(CASE WHEN department_id = 1 THEN 1 END) AS "Engineering",
	COUNT(CASE WHEN department_id = 2 THEN 1 END) AS "Tool Design",
	COUNT(CASE WHEN department_id = 3 THEN 1 END) AS "Sales",
	COUNT(CASE WHEN department_id = 4 THEN 1 END) AS "Marketing",
	COUNT(CASE WHEN department_id = 5 THEN 1 END) AS "Purchasing",
	COUNT(CASE WHEN department_id = 6 THEN 1 END) AS "Research and Development",
	COUNT(CASE WHEN department_id = 7 THEN 1 END) AS "Production"
FROM
	employees;



-- 14. Update Employees’ Data.
UPDATE
	employees
SET 
	salary = CASE
		WHEN hire_date < '2015-01-16' THEN salary + 2500
		WHEN hire_date < '2020-03-04' THEN salary + 1500
		ELSE salary
	END,
	job_title = CASE 
		WHEN hire_date < '2015-01-16' THEN 'Senior ' || job_title
		WHEN hire_date < '2020-03-04' THEN 'Mid-' || job_title
		ELSE job_title
	END;



-- 15. Categorizes Salary.
SELECT
	job_title,
	CASE 
		WHEN AVG(salary) > 45800 THEN 'Good'
		WHEN AVG(salary) BETWEEN 27500 AND 45800 THEN 'Medium'
		WHEN AVG(salary) < 27500 THEN 'Need Improvement'
	END AS "Category"
FROM
	employees
GROUP BY
	job_title
ORDER BY
	"Category" ASC,
	job_title ASC;



-- 16. WHERE Project Status.
SELECT
	project_name,
	CASE
		WHEN start_date IS NULL AND end_date IS NULL THEN 'Ready for development'
		WHEN end_date IS NULL THEN 'In Progress'
		ELSE 'Done'
	END AS project_status
FROM
	projects
WHERE
	project_name LIKE '%Mountain%';



-- 17. HAVING Salary Level.
SELECT
	department_id,
	COUNT(*) AS num_employees,
	CASE 
		WHEN AVG(salary) > 50000 THEN 'Above average'
		ELSE 'Below average'
	END AS salary_level
FROM
	employees
GROUP BY
	department_id
HAVING
	AVG(salary) > 30000
ORDER BY
	department_id;



-- 18. Nested CASE Conditions.
CREATE VIEW view_performance_rating AS
	SELECT
		first_name,
		last_name,
		job_title,
		salary,
		department_id,
		CASE 
			WHEN salary >= 25000 THEN (
				CASE
					WHEN job_title LIKE 'Senior%' THEN 'High-performing Senior'
					ELSE 'High-performing Employee'
				END)
			ELSE 'Average-performing'
		END AS performance_rating
	FROM
		employees;



-- 19. Foreign Key.
CREATE TABLE employees_projects (
	id INTEGER PRIMARY KEY,
	employee_id INTEGER,
	project_id INTEGER,
	CONSTRAINT fk_ep_employees
		FOREIGN KEY (employee_id)
		REFERENCES employees (id),
	CONSTRAINT fk_ep_projects
		FOREIGN KEY (project_id)
		REFERENCES projects (id)
);



-- 20. JOIN Tables.
SELECT
	d.id,
	d.department_name,
	d.manager_id,
	e.id,
	e.first_name,
	e.last_name,
	e.job_title,
	e.department_id,
	e.manager_id,
	e.hire_date,
	e.salary,
	e.address_id
FROM
	departments d
JOIN employees e 
	ON e.department_id = d.id;


