-- list
SELECT cities.id, cities.name, states.name FROM cities and states
WHERE cities.state_id = states.id
ORDER BY cities.id;
