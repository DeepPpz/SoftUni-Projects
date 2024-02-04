USE restaurant_db;


# 01. Table Design.
CREATE TABLE products (
	id INTEGER PRIMARY KEY AUTO_INCREMENT,
	name VARCHAR(30) NOT NULL UNIQUE,
	type VARCHAR(30) NOT NULL,
	price DECIMAL(10,2) NOT NULL
);

CREATE TABLE clients (
	id INTEGER PRIMARY KEY AUTO_INCREMENT,
	first_name VARCHAR(50) NOT NULL,
	last_name VARCHAR(50) NOT NULL,
	birthdate DATE NOT NULL,
	card VARCHAR(50),
	review TEXT
);

CREATE TABLE tables (
	id INTEGER PRIMARY KEY AUTO_INCREMENT,
	floor INTEGER NOT NULL,
	reserved BOOLEAN,
	capacity INTEGER NOT NULL
);

CREATE TABLE waiters (
	id INTEGER PRIMARY KEY AUTO_INCREMENT,
	first_name VARCHAR(50) NOT NULL,
	last_name VARCHAR(50) NOT NULL,
	email VARCHAR(50) NOT NULL,
	phone VARCHAR(50),
	salary DECIMAL(10,2)
);

CREATE TABLE orders (
	id INTEGER PRIMARY KEY AUTO_INCREMENT,
	table_id INTEGER NOT NULL,
	waiter_id INTEGER NOT NULL,
	order_time TIME NOT NULL,
	payed_status BOOLEAN,
	CONSTRAINT fk_orders_tables
		FOREIGN KEY (table_id)
		REFERENCES tables (id),
	CONSTRAINT fk_orders_waiters
		FOREIGN KEY (waiter_id)
		REFERENCES waiters (id)
);

CREATE TABLE orders_clients (
	order_id INTEGER,
	client_id INTEGER,
	CONSTRAINT fk_orders_clients_orders
		FOREIGN KEY (order_id)
		REFERENCES orders (id),
	CONSTRAINT fk_orders_clients_clients
		FOREIGN KEY (client_id)
		REFERENCES clients (id)
);

CREATE TABLE orders_products (
	order_id INTEGER,
	product_id INTEGER,
	CONSTRAINT fk_orders_products_orders
		FOREIGN KEY (order_id)
		REFERENCES orders (id),
	CONSTRAINT fk_orders_products_products
		FOREIGN KEY (product_id)
		REFERENCES products (id)
);


# 02. Insert.
INSERT INTO products (name, type, price)
	SELECT 
		CONCAT(last_name, ' ', 'specialty'), 'Cocktail', CEIL(salary * 0.01)
	FROM 
		waiters
	WHERE 
		id > 6;


# 03. Update.
UPDATE 
	orders
SET 
	table_id = table_id - 1
WHERE 
	id BETWEEN 12 AND 23;


# 04. Delete.
DELETE FROM 
	waiters
WHERE 
	id NOT IN (
    	SELECT 
        	DISTINCT waiter_id
    	FROM 
        	orders
);


# 05. Clients.
SELECT 
	*
FROM 
	clients
ORDER BY
	birthdate DESC,
	id DESC;


# 06. Birthdate.
SELECT 
	first_name,
	last_name,
	birthdate,
	review
FROM 
	clients
WHERE 
	card IS NULL 
	AND YEAR(birthdate) BETWEEN 1978 AND 1993
ORDER BY 
	last_name DESC,
	id ASC
LIMIT 5;


# 07. Accounts.
SELECT 
	CONCAT(last_name, first_name, CHAR_LENGTH(first_name), 'Restaurant') AS username,
	REVERSE(SUBSTRING(email, 2, 12)) AS password
FROM 
	waiters
WHERE 
	salary IS NOT NULL
ORDER BY 
	password DESC;


# 08. Top from Menu.
SELECT
	p.id, 
	p.name,
	COUNT(*) AS count
FROM
	products AS p
JOIN orders_products AS op
	ON op.product_id = p.id
JOIN orders AS o
	ON o.id = op.order_id
GROUP BY 
	p.id,
	p.name
HAVING 
	count >= 5
ORDER BY 
	count DESC,
	p.name ASC;


# 09. Availability.
SELECT 
	t.id AS table_id,
	t.capacity,
	COUNT(oc.client_id) AS count_clients,
	CASE
		WHEN COUNT(oc.client_id) < t.capacity THEN 'Free seats'
		WHEN COUNT(oc.client_id) = t.capacity THEN 'Full'
		ELSE 'Extra seats'
	END AS availability
FROM 
	tables AS t
LEFT JOIN orders AS o 
	ON o.table_id = t.id
JOIN orders_clients AS oc
	ON oc.order_id = o.id
WHERE 
	t.floor = 1
GROUP BY 
	t.id, 
	t.capacity
ORDER BY 
	table_id DESC;


# 10. Extract bill.
CREATE FUNCTION udf_client_bill(full_name VARCHAR(50))
RETURNS DECIMAL(19,2)
DETERMINISTIC

BEGIN
	RETURN (
		SELECT 
			SUM(p.price) AS bill
		FROM
			clients AS c
		JOIN orders_clients AS oc 
			ON oc.client_id = c.id
		JOIN orders AS o 
			ON o.id = oc.order_id
		JOIN orders_products AS op 
			ON op.order_id = o.id
		JOIN products AS p 
			ON p.id = op.product_id
		WHERE
			CONCAT_WS(' ', c.first_name, c.last_name) = full_name
		GROUP BY 
			c.id
    );
END


# 11. Happy hour.
CREATE PROCEDURE udp_happy_hour(type VARCHAR(50))

BEGIN
	UPDATE 
		products AS p 
	SET 
		p.price = p.price * 0.8
	WHERE
		p.price >= 10 and p.type = type;
END
