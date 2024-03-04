#List all car brands where the average mileage is greater than 100,000.
SELECT Brand FROM arvind.cars GROUP BY Brand HAVING AVG(Mileage)>100000