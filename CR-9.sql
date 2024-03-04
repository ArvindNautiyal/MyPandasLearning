#Find the brand and model of the oldest car (based on the year) in the dataset.
SELECT Brand , Model , Year FROM arvind.cars ORDER BY Year ASC LIMIT 1