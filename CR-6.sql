#Show the top 5 car brands with the highest average price.
SELECT Brand , AVG(Price) AS "AVGP" FROM arvind.cars GROUP BY Brand ORDER BY AVGP DESC LIMIT 5