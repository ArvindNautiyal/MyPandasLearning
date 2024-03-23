-- CASE STUDY ON FLIGHT DATASET

USE projects;

-- Find the month with most number of flights 

SELECT MONTHNAME(Date_of_Journey) AS Month_Name , COUNT(*) AS Total_flights FROM flights
GROUP BY Month_Name
ORDER BY Total_flights DESC LIMIT 1;

-- Which Week day has the most costly flight price

SELECT DAYOFWEEK(Date_of_Journey)  AS "Day_Of_Week" , AVG(Price) AS Avg_Week_Price FROM flights
GROUP BY Day_Of_Week
ORDER BY Avg_Week_Price DESC LIMIT 1;


-- Find Number of INDIGO fligth every month

SELECT MONTHNAME(Date_of_Journey) AS Month_Name , COUNT(*) AS Flight_count FROM flights
WHERE Airline IN ("Indigo")
GROUP BY Month_Name;



-- Find list of all flights that depart between 10AM and 2PM from  Banglore to Delhi

SELECT * FROM flights
WHERE Source = "Banglore" AND Destination = "Delhi" 
AND Dep_Time BETWEEN "10:00:00" AND "14:00:00";


-- Find the flights departing on weekends from Bangalore

SELECT * , DAYNAME(Date_of_Journey) FROM flights
WHERE Source = "Banglore" AND 
DAYNAME(Date_of_Journey) IN ("Sunday" ,"Satirday");


-- Calculate the arrival time for all flights by adding the duration to the departure time.

ALTER TABLE flights ADD COLUMN departure_time DATETIME;

UPDATE flights
SET departure_time =  (STR_TO_DATE(CONCAT(Date_of_Journey, " " , Dep_Time),"%Y-%m-%d %H:%i"));

ALTER TABLE flights ADD COLUMN duration_min INTEGER;
ALTER TABLE flights ADD COLUMN arrival DATETIME;

UPDATE flights
SET duration_min = (CASE 
						WHEN Duration LIKE "%h%m" THEN 
                        SUBSTRING_INDEX(Duration,"h",1)*60 + 
                        SUBSTRING_INDEX(SUBSTRING_INDEX(Duration,"m",-1),"m",1)
                        WHEN Duration LIKE "%h" THEN
                        SUBSTRING_INDEX(Duration,"h",1)*60
                        WHEN Duration LIKe "%m" THEN
                        SUBSTRING_INDEX(Duration,"m",1)
					END);


UPDATE flights
SET arrival = DATE_ADD(departure_time, INTERVAL duration_min MINUTE);
SELECT * FROM flights;

-- Calculate the arrival date for all the flights

SELECT DATE(arrival) FROM flights;



-- Find the number of flights which travel on multiple dates.

SELECT COUNT(*) FROM flights
WHERE DATE(departure_time) != DATE(arrival);

-- Calculate the average duration of flights between all city pairs. 

SELECT Source , Destination ,
 DATE_FORMAT(SEC_TO_TIME(AVG(duration_min)*60),"%kh %im") AS Avg_duration FROM flights
GROUP BY Source , Destination;



-- Find all flights which departed before midnight but arrived at their destination after midnight having only 0 stops.

SELECT * FROM flights
WHERE Total_Stops = 'non-stop' AND 
HOUR(departure_time) >= 18 AND HOUR(arrival) <=12;



-- Find quarter wise number of flights for each airline

SELECT Airline , QUARTER(departure_time) AS Quart ,
COUNT(*) AS Quater_wise_count FROM flights
GROUP BY Airline , QUARTER(departure_time);

-- Find the longest flight distance(between cities in terms of time) in India

SELECT Source , Destination , ROUND(AVG(Duration),0) AS AVG_DURATION FROM flights
GROUP BY Source , Destination
ORDER BY AVG(Duration) DESC;

-- Average time duration for flights that have 1 stop vs more than 1 stops

SELECT AVG(duration_min) FROM flights
WHERE Total_Stops = '1 stop'
UNION 
SELECT AVG(duration_min) FROM flights
WHERE Total_Stops != "non-stop" AND Total_Stops != "1 stop";


-- Find all Air India flights in a given date range originating from Delhi 3 JAN - 18 MAY

SELECT * FROM flights
WHERE Source = "Delhi" AND DATE(departure_time) BETWEEN "2019-03-15" AND "2019-05-18";

-- Find the longest flight of each airline

SELECT Airline ,  DATE_FORMAT(SEC_TO_TIME(MAX(duration_min)*60),"%kh %im") AS Longest_hours FROM flights
GROUP BY Airline ;

-- Find all the pair of cities having average time duration > 3 hours


SELECT Source , Destination , DATE_FORMAT(SEC_TO_TIME((AVG(duration_min)*60)),"%kh") AS Time FROM flights
GROUP BY Source , Destination
HAVING  DATE_FORMAT(SEC_TO_TIME((AVG(duration_min)*60)),"%kh") > 3;


-- Make a weekday vs time grid showing frequency of flights from Banglore and Delhi

SELECT DAYNAME(Date_of_Journey) AS Week,
SUM(CASE WHEN HOUR(Date_of_Journey) BETWEEN 0 AND 5 THEN 1 ELSE 0 END) AS "12AM-6AM",
SUM(CASE WHEN HOUR(Date_of_Journey) BETWEEN 6 AND 11 THEN 1 ELSE 0 END) AS "6AM-12AM",
SUM(CASE WHEN HOUR(Date_of_Journey) BETWEEN 12 AND 17 THEN 1 ELSE 0 END) AS "12PM-6PM",
SUM(CASE WHEN HOUR(Date_of_Journey) BETWEEN 18 AND 23 THEN 1 ELSE 0 END) AS "6PM-12AM"
FROM flights
WHERE Source = 'Bangalore' AND Destination = 'Delhi'
GROUP BY DAYNAME(Date_of_Journey);

-- Thank you



























