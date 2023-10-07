-- 01. Count Employees by Town.
CREATE FUNCTION fn_count_employees_by_town (town_name VARCHAR(20))
RETURNS INT
AS $$
DECLARE e_count INT;

BEGIN
	SELECT
		COUNT(employee_id) INTO e_count
	FROM
		employees AS e
	JOIN addresses AS a
		ON a.address_id = e.address_id
	JOIN towns AS t 
		ON t.town_id = a.town_id
	WHERE
		t.name = town_name;
	
	RETURN e_count;
END;

$$ LANGUAGE plpgsql;



-- 02. Employees Promotion.
CREATE PROCEDURE sp_increase_salaries(department_name VARCHAR(50))
AS $$

BEGIN
	UPDATE employees AS e
	SET salary = salary * 1.05
	WHERE department_id = (
		SELECT 
			department_id
		FROM
			departments
		WHERE
			name = department_name
		);
END;

$$ LANGUAGE plpgsql;



-- 03. Employees Promotion By ID.
CREATE PROCEDURE sp_increase_salary_by_id(id INT)
AS $$

BEGIN
	IF (
		SELECT
			COUNT(employee_id)
		FROM
			employees
		WHERE
			employee_id = id
		) <> 1 THEN
		ROLLBACK;
	ELSE
		UPDATE employees
		SET salary = salary * 1.05
		WHERE employee_id = id;
	END IF;

	COMMIT;
END;

$$ LANGUAGE plpgsql;



-- 04. Triggered.
CREATE TABLE deleted_employees (
	employee_id SERIAL PRIMARY KEY,
	first_name VARCHAR(50),
	last_name VARCHAR(50),
	middle_name VARCHAR(50),
	job_title varchar(50),
	department_id INT,
	salary numeric(19,4)
);


CREATE FUNCTION trigger_fn_on_employee_delete() 
RETURNS TRIGGER
AS $$

BEGIN
	INSERT INTO deleted_employees (
			first_name, last_name,
			middle_name, job_title,
			department_id, salary)
	VALUES
		(OLD.first_name, OLD.last_name,
		OLD.middle_name, OLD.job_title,
		OLD.department_id, OLD.salary);
	
	RETURN NULL;
END;

$$ LANGUAGE plpgsql;


CREATE TRIGGER tr_deleted_employees
AFTER DELETE 
	ON employees
FOR EACH ROW 
EXECUTE FUNCTION 
	trigger_fn_on_employee_delete();


