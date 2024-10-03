SELECT * FROM
(
SELECT
CAST(strftime('%W', timestamp) AS INTEGER) AS week_of_year,
CAST(strftime('%u', timestamp) AS INTEGER) AS day_of_week,
product_id,
year(release_date) release_year
FROM
activity a
INNER JOIN categories c
ON c.category_id = a.category_id
) temp_table
PIVOT (
COUNT (product_id)
FOR category_name IN (
Mobile,
Headphone,
Tablet)
) pivot_table;
