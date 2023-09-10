-- average
SELECT city, AVG(value) AS v FROM temperatures
GROUP BY city
ORDER BY v DESC;
