-- 1.1. Database Design.
CREATE TABLE towns (
	id SERIAL PRIMARY KEY,
	name VARCHAR(45) NOT NULL
);


CREATE TABLE stadiums (
	id SERIAL PRIMARY KEY,
	name VARCHAR(45) NOT NULL,
	capacity INT NOT NULL CHECK (capacity > 0),
	town_id INT NOT NULL,
	CONSTRAINT fk_stadiums_towns
		FOREIGN KEY (town_id)
		REFERENCES towns (id)
		ON DELETE CASCADE
		ON UPDATE CASCADE
);


CREATE TABLE teams (
	id SERIAL PRIMARY KEY,
	name VARCHAR(45) NOT NULL,
	established DATE NOT NULL,
	fan_base INT NOT NULL DEFAULT 0 CHECK (fan_base >= 0),
	stadium_id INT NOT NULL,
	CONSTRAINT fk_teams_stadiums
		FOREIGN KEY (stadium_id)
		REFERENCES stadiums (id)
		ON DELETE CASCADE
		ON UPDATE CASCADE
);


CREATE TABLE coaches (
	id SERIAL PRIMARY KEY,
	first_name VARCHAR(10) NOT NULL,
	last_name VARCHAR(20) NOT NULL,
	salary NUMERIC(10,2) NOT NULL DEFAULT 0 CHECK (salary >= 0),
	coach_level INT NOT NULL DEFAULT 0 CHECK (coach_level >= 0)
);


CREATE TABLE skills_data (
	id SERIAL PRIMARY KEY,
	dribbling INT DEFAULT 0 CHECK (dribbling >= 0),
	pace INT DEFAULT 0 CHECK (pace >= 0),
	passing INT DEFAULT 0 CHECK (passing >= 0),
	shooting INT DEFAULT 0 CHECK (shooting >= 0),
	speed INT DEFAULT 0 CHECK (speed >= 0),
	strength INT DEFAULT 0 CHECK (strength >= 0)
);


CREATE TABLE players (
	id SERIAL PRIMARY KEY,
	first_name VARCHAR(10) NOT NULL,
	last_name VARCHAR(20) NOT NULL,
	age INT NOT NULL DEFAULT 0 CHECK (age >= 0),
	position CHAR(1) NOT NULL,
	salary NUMERIC(10,2) NOT NULL DEFAULT 0 CHECK (salary >= 0),
	hire_date TIMESTAMP,
	skills_data_id INT NOT NULL,
	team_id INT,
	CONSTRAINT fk_players_skills_data
		FOREIGN KEY (skills_data_id)
		REFERENCES skills_data (id)
		ON DELETE CASCADE
		ON UPDATE CASCADE,
	CONSTRAINT fk_players_teams
		FOREIGN KEY (team_id)
		REFERENCES teams (id)
		ON DELETE CASCADE
		ON UPDATE CASCADE
);


CREATE TABLE players_coaches (
	player_id INT,
	coach_id INT,
	CONSTRAINT fk_players_coaches_players
		FOREIGN KEY (player_id)
		REFERENCES players (id)
		ON DELETE CASCADE
		ON UPDATE CASCADE,
	CONSTRAINT fk_players_coaches_coaches
		FOREIGN KEY (coach_id)
		REFERENCES coaches (id)
		ON DELETE CASCADE
		ON UPDATE CASCADE
);



-- 2.2. Insert.
INSERT INTO coaches (first_name, last_name, salary, coach_level)
	SELECT
		first_name,
		last_name,
		(salary * 2),
		CHAR_LENGTH(first_name)
	FROM 
		players
	WHERE 
		hire_date < '2013-12-13 07:18:46';



-- 2.3. Update.
UPDATE 
	coaches
SET 
	salary = salary * coach_level
WHERE 
	first_name LIKE 'C%'
	AND id IN (
		SELECT 
			id
		FROM 
			players_coaches
		GROUP BY
			coach_id
		HAVING 
			COUNT(*) >=1
		);


-- 2.4. Delete.
DELETE FROM 
	players_coaches
WHERE 
	player_id IN (
		SELECT 
			id
		FROM
			players
		WHERE 
			hire_date < '2013-12-13 07:18:46'
		);


DELETE FROM 
	players
WHERE 
	hire_date < '2013-12-13 07:18:46';



-- 3.5. Players.
SELECT
	CONCAT(first_name, ' ', last_name) AS full_name,
	age,
	hire_date
FROM 
	players
WHERE 
	first_name LIKE 'M%'
ORDER BY 
	age DESC,
	full_name ASC; 


-- 3.6. Offensive Players without Team.
SELECT 
	p.id,
	CONCAT(p.first_name, ' ', p.last_name) AS full_name,
	p.age,
	p.position,
	p.salary,
	sd.pace,
	sd.shooting
FROM
	players p
JOIN skills_data sd
	ON sd.id = p.skills_data_id
WHERE 
	p.position = 'A'
	AND team_id IS NULL
	AND (sd.pace + sd.shooting) > 130;



-- 3.7. Teams with Player Count and Fan Base.
SELECT
	t.id AS team_id,
	t.name AS team_name,
	COUNT(p.id) AS player_count,
	t.fan_base
FROM 
	teams t
LEFT JOIN players p
	ON p.team_id = t.id
WHERE 
	t.fan_base > 30000
GROUP BY
	t.id,
	t.name,
	t.fan_base
ORDER BY 
	player_count DESC,
	t.fan_base DESC;



-- 3.8. Coaches, Players Skills and Teams Overview.
SELECT 
	CONCAT(c.first_name, ' ', c.last_name) AS coach_full_name,
	CONCAT(p.first_name, ' ', p.last_name) AS player_full_name,
	t.name AS team_name,
	sd.passing,
	sd.shooting,
	sd.speed
FROM
	coaches c
JOIN players_coaches pc
	ON pc.coach_id = c.id
JOIN players p
	ON p.id = pc.player_id
JOIN teams t
	ON t.id = p.team_id
JOIN skills_data sd
	ON sd.id = p.skills_data_id
ORDER BY 
	coach_full_name ASC,
	player_full_name DESC;



-- 4.9. Stadium Teams Information.
CREATE OR REPLACE FUNCTION fn_stadium_team_name(stadium_name VARCHAR(30))
RETURNS TABLE (team_name VARCHAR(100))
AS $$

BEGIN
	RETURN QUERY
	SELECT 
		t.name
	FROM 
		teams t
	JOIN stadiums s	
		ON s.id = t.stadium_id
	WHERE 
		s.name = stadium_name
	ORDER BY
		t.name ASC;
END;

$$ LANGUAGE plpgsql;



-- 4.10. Player Team Finder.
CREATE OR REPLACE PROCEDURE sp_players_team_name(IN player_name VARCHAR(50),
												OUT team_name VARCHAR(45))
AS $$

BEGIN
	SELECT 
		COALESCE(t.name, 'The player currently has no team') INTO team_name
	FROM
		players p
	LEFT JOIN teams t
		ON t.id = p.team_id
	WHERE 
		CONCAT(p.first_name, ' ', p.last_name) = player_name;
END;

$$ LANGUAGE plpgsql;


