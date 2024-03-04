#Retrieve the total count of cars for each year in the dataset.
SELECT Year , COUNT(*) AS "TOTAL_C" FROM arvind.cars GROUP BY Year 
