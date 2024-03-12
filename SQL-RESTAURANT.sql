USE projects;

#Fetching random values form users tabel

SELECT * FROM users ORDER BY rand() LIMIT 5;

#finding null values

SELECT * FROM orders WHERE restaurant_rating IS NULL;

#finding orders placed by each costumers

SELECT t1.name , t1.user_id  , COUNT(*) AS "Total_order_placed" FROM users t1
JOIN orders t2
ON t1.user_id = t2.user_id
GROUP BY t2.user_id,t1.name;

#restaurant selling most number of items

SELECT t1.r_id, COUNT(*) AS "TOTAL_ITEM" FROM menu t1
JOIN restaurants t2
ON t1.r_id = t2.r_id
GROUP BY t1.r_id;

#find number of votes and average ratings of all restaurants

SELECT t2.r_id ,t2.r_name, COUNT(*) AS "TOTAL_VOTES" , ROUND(AVG(restaurant_rating),2) AS "AVERAGE_RATING" 
FROM orders t1
JOIN restaurants t2
ON t1.r_id = t2.r_id
WHERE restaurant_rating IS NOT NULL
GROUP BY t1.r_id ,t2.r_name;

#find the food that is most time ordered

SELECT t1.f_name , COUNT(*) AS "Total_Order" FROM food t1
JOIN order_details t2
ON t1.f_id = t2.f_id
GROUP BY t1.f_name
ORDER BY Total_Order DESC LIMIT 1;

#find restaurant with maximum revenue in month may

SELECT t1.r_id , t1.r_name,SUM(amount) AS "Total_Amount"  FROM restaurants t1
JOIN orders t2
ON t1.r_id = t2.r_id
WHERE MONTHNAME(DATE(date)) = "May"
GROUP BY t1.r_id , t1.r_name
ORDER BY Total_Amount DESC LIMIT 1;

#find restaurant with maximum revenue in all month

SELECT t1.r_id , t1.r_name,SUM(amount) AS "Total_Amount"  FROM restaurants t1
JOIN orders t2
ON t1.r_id = t2.r_id
WHERE MONTHNAME(DATE(date)) IN ("May","June","July")
GROUP BY t1.r_id , t1.r_name
ORDER BY Total_Amount DESC;

#find restaurant revenue  month wise

SELECT t1.r_id , t1.r_name,SUM(amount) AS "Total_Amount", 
MONTHNAME(DATE(date)) AS "Month"  FROM restaurants t1
JOIN orders t2
ON t1.r_id = t2.r_id
GROUP BY t1.r_id , t1.r_name,MONTHNAME(DATE(date))
ORDER BY Total_Amount DESC;

# find all restaurant whose total sales are greater than 1500

SELECT t1.r_id, t1.r_name , SUM(amount) AS "Total_Income" FROM restaurants t1
JOIN orders t2
ON t1.r_id = t2.r_id
GROUP BY t1.r_id, t1.r_name
HAVING Total_Income > 1500;

# find customers id who have never ordered

SELECT user_id 
FROM users
EXCEPT
SELECT t1.user_id
FROM orders t1
JOIN users t2 ON t1.user_id = t2.user_id;

#Show order details of particular order

SELECT t1.user_id , t1.date ,t3.f_name ,t4.r_name FROM orders t1
JOIN order_details t2
ON t1.order_id = t2.order_id
JOIN food t3
ON t3.f_id = t2.f_id
JOIN restaurants t4
ON t4.r_id = t1.r_id
WHERE t1.user_id = 1 AND date BETWEEN "2022-05-10" AND "2022-06-15"
ORDER BY date;

# Customer favortie food

SELECT  COUNT(*) AS "order" , t2.user_id  , t3.f_name FROM order_details t1
JOIN orders t2
ON t1.order_id = t2.order_id
JOIN food t3
ON t3.f_id = t1.f_id
GROUP BY  t2.user_id ,t3.f_name
ORDER BY COUNT(*) DESC;

# find most coslty restaurant

SELECT t2.r_name , SUM(price)/COUNT(*) AS "Average_Price" FROM menu t1
JOIN restaurants t2
ON t1.r_id = t2.r_id
GROUP BY t1.r_id , t2.r_name
ORDER BY Average_Price DESC;

#Delivey partner compensation or salary

SELECT t1.partner_name , ROUND(((COUNT(*) * 100) + (1000*AVG(delivery_rating))),2) AS "Salary" 
FROM delivery_partner t1
JOIN orders t2
ON t1.partner_id = t2.partner_id
GROUP BY t1.partner_id, t1.partner_name;

# Find all veg restaurants

SELECT t4.r_id , t1.type FROM food t1
JOIN order_details t2
ON t1.f_id = t2.f_id
JOIN orders t3
ON t3.order_id = t2.order_id
JOIN restaurants t4
ON t4.r_id = t3.r_id
WHERE t1.type NOT IN  ("Non-Veg")
GROUP BY t4.r_id , t1.type;

# Find Min and Max Value of Customer order

SELECT r_id , MAX(amount) AS "MIN_ORDER_PRICE", MIN(amount) AS "MAX_ORDER_PRICE" FROM orders
GROUP BY r_id;




#