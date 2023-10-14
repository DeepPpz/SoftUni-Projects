-- 01. Booked for Nights.
SELECT 
	CONCAT(a.address, ' ', a.address_2) AS "Apartment Address",
	b.booked_for AS "Nights"
FROM 
	apartments a 
JOIN bookings b 
	ON b.booking_id = a.booking_id 
ORDER BY 
	a.apartment_id;



-- 02. First 10 Apartments Booked At.
SELECT 
	a.name AS "Name",
	a.country AS "Country",
	DATE(b.booked_at) AS "Booked at"
FROM 
	apartments a
LEFT JOIN bookings b 
	ON b.booking_id = a.booking_id
ORDER BY 
	a.apartment_id
LIMIT 10;



-- 03. First 10 Customers with Bookings.
SELECT 
	b.booking_id AS "Booking ID",
	DATE(b.starts_at) AS "Start Date",
	b.apartment_id AS "Apartment ID",
	CONCAT(c.first_name, ' ', c.last_name) AS "Customer Name"
FROM 
	bookings b 
RIGHT JOIN customers c 
	ON c.customer_id = b.customer_id 
ORDER BY 
	"Customer Name" ASC
LIMIT 10;



-- 04. Booking Information.
SELECT 
	b.booking_id AS "Booking ID",
	a.name AS "Apartment Owner",
	a.apartment_id AS "Apartment ID",
	CONCAT(c.first_name, ' ', c.last_name) AS "Customer Name"
FROM 
	bookings b
FULL JOIN apartments a 
	ON a.booking_id = b.booking_id 
FULL JOIN customers c 
	ON c.customer_id = b.customer_id 
ORDER BY 
	"Booking ID",
	"Apartment Owner",
	"Customer Name";



-- 05. Multiplication of Information.
SELECT 
	b.booking_id AS "Booking ID",
	c.first_name AS "Customer Name"
FROM 
	bookings b 
CROSS JOIN customers c 
ORDER BY 
	"Customer Name";



-- 06. Unassigned Apartments.
SELECT 
	b.booking_id,
	b.apartment_id,
	c.companion_full_name
FROM 
	bookings b 
LEFT JOIN customers c 
	USING (customer_id)
WHERE 
	b.apartment_id IS NULL;



-- 07. Bookings Made by Lead.
SELECT 
	b.apartment_id,
	b.booked_for,
	c.first_name,
	c.country
FROM 
	bookings b 
JOIN customers c 
	USING (customer_id)
WHERE 
	c.job_type = 'Lead';



-- 08. Hahn`s Bookings.
SELECT 
	COUNT(*) AS "count"
FROM 
	bookings b 
JOIN customers c 
	USING (customer_id)
WHERE 
	c.last_name = 'Hahn';



-- 09. Total Sum of Nights.
SELECT 
	a.name,
	SUM(b.booked_for) AS "sum"
FROM 
	apartments a 
JOIN bookings b 
	USING (apartment_id)
GROUP BY 
	a.name
ORDER BY 
	a.name ASC;



-- 10. Popular Vacation Destination.
SELECT 
	a.country,
	COUNT(b.booking_id) AS booking_count
FROM 
	apartments a
JOIN bookings b 
	ON b.apartment_id = a.apartment_id 
WHERE 
	b.booked_at > '2021-05-18 07:52:09.904+03' 
	AND b.booked_at < '2021-09-17 19:48:02.147+03'
GROUP BY
	a.country
ORDER BY 
	booking_count DESC;



-- 11. Bulgaria's Peaks Higher than 2835 Meters.
SELECT 
	mc.country_code,
	m.mountain_range,
	p.peak_name,
	p.elevation
FROM 
	mountains m 
JOIN mountains_countries mc 
	ON mc.mountain_id = m.id 
JOIN peaks p 
	ON p.mountain_id = m.id
WHERE 
	p.elevation > 2835
	AND mc.country_code = 'BG'
ORDER BY 
	elevation DESC;



-- 12. Count Mountain Ranges.
SELECT 
	mc.country_code,
	COUNT(DISTINCT m.mountain_range) AS mountain_range_count
FROM 
	mountains_countries mc 
JOIN mountains m 
	ON m.id = mc.mountain_id
WHERE 
	country_code IN ('US', 'RU', 'BG')
GROUP BY 
	country_code 
ORDER BY 
	mountain_range_count DESC;



-- 13. Rivers in Africa.
SELECT 
	c.country_name,
	r.river_name
FROM 
	countries c 
LEFT JOIN countries_rivers cr
	ON cr.country_code = c.country_code 
LEFT JOIN rivers r 
	ON r.id = cr.river_id
WHERE 
	c.continent_code = 'AF'
ORDER BY 
	c.country_name ASC 
LIMIT 5;



-- 14. Minimum Average Area Across Continents.
SELECT 
	MIN(average_area) AS min_average_area
FROM (
	SELECT 
		cou.continent_code,
		AVG(cou.area_in_sq_km) AS average_area
	FROM 
		countries cou
	GROUP BY 
		cou.continent_code
	) AS continent_area;



-- 15. Countries Without Any Mountains.
SELECT 
	COUNT(*) AS countries_without_mountains
FROM 
	countries c 
LEFT JOIN mountains_countries mc 
	ON mc.country_code = c.country_code 
WHERE 
	mc.mountain_id IS NULL;



-- 16. Monasteries by Country.
CREATE TABLE monasteries (
	id SERIAL PRIMARY KEY,
	monastery_name VARCHAR(255),
	country_code CHAR(2),
	CONSTRAINT fk_monasteries_countries
		FOREIGN KEY (country_code)
		REFERENCES countries (country_code)
);


INSERT INTO monasteries (monastery_name, country_code)
VALUES
	('Rila Monastery "St. Ivan of Rila"', 'BG'),
	('Bachkovo Monastery "Virgin Mary"', 'BG'),
	('Troyan Monastery "Holy Mother''s Assumption"', 'BG'),
	('Kopan Monastery', 'NP'),
	('Thrangu Tashi Yangtse Monastery', 'NP'),
	('Shechen Tennyi Dargyeling Monastery', 'NP'),
	('Benchen Monastery', 'NP'),
	('Southern Shaolin Monastery', 'CN'),
	('Dabei Monastery', 'CN'),
	('Wa Sau Toi', 'CN'),
	('Lhunshigyia Monastery', 'CN'),
	('Rakya Monastery', 'CN'),
	('Monasteries of Meteora', 'GR'),
	('The Holy Monastery of Stavronikita', 'GR'),
	('Taung Kalat Monastery', 'MM'),
	('Pa-Auk Forest Monastery', 'MM'),
	('Taktsang Palphug Monastery', 'BT'),
	('Sümela Monastery', 'TR');


ALTER TABLE countries
	ADD COLUMN three_rivers BOOLEAN DEFAULT FALSE;


UPDATE
	countries c
SET
	three_rivers = TRUE
WHERE (
	SELECT
		COUNT(*)
	FROM
		countries_rivers cr
	WHERE
		cr.country_code = c.country_code
	) > 3;


SELECT
	m.monastery_name AS "Monastery",
	c.country_name AS "Country"
FROM
	monasteries m
JOIN countries c
	USING (country_code)
WHERE
	c.three_rivers IS FALSE
ORDER BY
	"Monastery";



-- 17. Monasteries by Continents and Countries.
UPDATE
	countries
SET
	country_name = 'Burma'
WHERE
	country_name = 'Myanmar';


INSERT INTO monasteries (monastery_name, country_code)
VALUES
	('Hanga Abbey', 'TZ');

	
SELECT
	con.continent_name AS "Continent Name",
	cou.country_name AS "Country Name",
	COUNT(m.id) AS "Monasteries Count"
FROM
	countries cou
LEFT JOIN continents con
	USING (continent_code)
LEFT JOIN monasteries m
	USING (country_code)
WHERE
	cou.three_rivers IS FALSE
GROUP BY
	cou.country_name,
	con.continent_name
ORDER BY
	"Monasteries Count" DESC,
	"Country Name" ASC;



-- 18. Retrieving Information about Indexes.
SELECT
	tablename,
	indexname,
	indexdef
FROM
	pg_indexes
WHERE
	schemaname = 'public'
ORDER BY
	tablename ASC,
	indexname ASC;



-- 19. Continents and Currencies.
CREATE VIEW continent_currency_usage AS
	WITH ranked_currency AS (
		SELECT 
			continent_code,
			currency_code,
			currency_usage,
			DENSE_RANK() OVER (PARTITION BY 
					continent_code ORDER BY currency_usage DESC) AS "rank"
		FROM (
			SELECT 
				continent_code, 
				currency_code,
				COUNT(*) AS currency_usage
			FROM
				countries
			GROUP BY 
				continent_code,
				currency_code
			HAVING COUNT(*) > 1
			) AS currency_counter
		)
	SELECT 
		continent_code,
		currency_code,
		currency_usage
	FROM 
		ranked_currency
	WHERE
		"rank" = 1
	ORDER BY
		currency_usage DESC,
		continent_code ASC,
		currency_code ASC;



-- 20. The Highest Peak in Each Country.
WITH row_number AS (
	SELECT 
		c.country_name,
		p.peak_name AS highest_peak,
		p.elevation AS highest_elevation,
		m.mountain_range,
		ROW_NUMBER() OVER (PARTITION BY 
				c.country_name ORDER BY p.elevation DESC) AS peak_rank
	FROM 
		countries c
	LEFT JOIN mountains_countries mc 
		ON mc.country_code = c.country_code
	LEFT JOIN peaks p 
		ON p.mountain_id = mc.mountain_id
	LEFT JOIN mountains m 
		ON m.id = p.mountain_id
	)
SELECT 
	country_name AS "Country",
	COALESCE(highest_peak, '(no highest peak)') AS "Highest Peak Name",
	COALESCE(highest_elevation, 0) AS "Highest Peak Elevation",
	COALESCE(mountain_range, '(no mountain)') AS "Mountain"
FROM 
	row_number
WHERE 
	peak_rank = 1
ORDER BY 
	"Country" ASC,
	"Highest Peak Elevation" DESC;


