-- Import in hbtn_0c_0 database this table
SELECT city, AVG(temperature) AS avg_temp
FROM temperatures
WHERE MONTH(date) IN (7, 8)
GROUP BY city
ORDER BY avg_temp DESC
LIMIT 3;
