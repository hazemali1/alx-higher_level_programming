-- average
SELECT city, AVG(value) AS v FROM temperature
GROUP BY city
ORDER BY v DESC;
