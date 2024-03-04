#List all car brands with their average price, but only show those brands with an average price above $20,000.
SELECT Brand , AVG(Price) AS "AVGP" FROM arvind.cars GROUP BY Brand  HAVING AVGP > 20000