-- 01. Find Book Titles.
SELECT
	title
FROM
	books
WHERE
	SUBSTRING(title, 1, 3) = 'The';



-- 02. Replace Titles.
SELECT
	REPLACE(title, SUBSTRING(title, 1, 3), '***') AS title
FROM
	books
WHERE
	SUBSTRING(title, 1, 3) = 'The';



-- 03. Triangles on Bookshelves.
SELECT
	id,
	((side * height) / 2) AS area
FROM
	triangles;



-- 04. Format Costs.
SELECT
	title,
	TO_CHAR(ROUND(cost, 3), '9999999999999.000') AS modified_price
FROM
	books;



-- 05. Year of Birth.
SELECT
	first_name,
	last_name,
	EXTRACT(YEAR FROM born) as year
FROM
	authors;



-- 06. Format Date of Birth.
SELECT
	last_name AS "Last Name",
	TO_CHAR(born, 'DD (Dy) Mon YYYY') AS "Date of Birth"
FROM
	authors;



-- 07. Harry Potter Books.
SELECT
	title
FROM
	books
WHERE
	title LIKE 'Harry%';


