#Display the car models with their average mileage, ordered by the highest mileage first.
SELECT Model , AVG(Mileage) AS "AVG_M" FROM arvind.cars GROUP BY Model ORDER BY AVG_M DESC 