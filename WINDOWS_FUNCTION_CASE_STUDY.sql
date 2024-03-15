USE projects;

SELECT * FROM insurance;
# Problem 1: What are the top 5 patients who claimed the highest insurance amounts?

SELECT * FROM (SELECT * , DENSE_RANK() OVER(ORDER BY claim DESC)  AS "Rank" FROM insurance) t
WHERE t.Rank <= 5;

# Problem 2: What is the average insurance claimed by patients based on the number of children they have?
SELECT * , AVG(claim) OVER(PARTITION BY children) FROM insurance;

# Problem 3: What is the highest and lowest claimed amount by patients in each region?

SELECT * , MAX(claim) OVER(PARTITION BY region) AS "MAX_CLAIM",
MIN(claim) OVER(PARTITION BY region) AS "MIN_CLAIM" FROM insurance;

# Problem 4: What is the percentage of smokers in each age group?

SELECT * , (COUNT(*) OVER(PARTITION BY age)) * 0.1 AS "Smoker_count" FROM insurance
WHERE smoker = "Yes";

#Problem 5: What is the difference between the claimed amount of each patient and the first claimed amount of that patient?

SELECT * ,claim -  LAG(claim) OVER()  FROM insurance;

#Problem 6: For each patient, calculate the difference between their claimed amount and 
-- the average claimed amount of patients with the same number of children.

SELECT * , ROUND((AVG(claim) OVER(PARTITION BY children) - claim ),2) AS "Claim_Difference" FROM insurance;

#Problem 7: Show the patient with the highest BMI in each region and their respective rank.

SELECT * , DENSE_RANK() OVER(PARTITION BY region ORDER BY bmi DESC) AS  "BMI_RANK" FROM insurance;

# Problem 8: Calculate the difference between the claimed amount of each patient and 
-- the claimed amount of the patient who has the highest BMI in their region.

SELECT * FROM (SELECT * , FIRST_VALUE(claim) OVER(PARTITION BY region ORDER BY bmi DESC) AS "RANK" FROM insurance ) t
WHERE t.RANK = 1

# Problem 9: For each patient, find the maximum BMI value among their next three records (ordered by age).

SELECT  * , MAX(bmi)  OVER(ORDER BY age ASC ROWS BETWEEN 1 FOLLOWING AND 3 FOLLOWING)  AS "Mac_bmi" FROM insurance;


-- Problem 10: For each patient, find the rolling average of the last 2 claims.

SELECT * , AVG(claim) OVER(ROWS BETWEEN 2 PRECEDING  AND 1 PRECEDING  ) FROM insurance;

# Problem 11: Find the first claimed insurance value for male and female patients, 
-- within each region order the data by patient age in ascending order, 
-- and only include patients who are non-diabetic and have a bmi value between 25 and 30.

SELECT * FROM(SELECT * , FIRST_VALUE(claim) OVER(PARTITION BY region , gender ORDER BY age) AS "FIRST_VALUE" FROM insurance) t
WHERE t.diabetic = "Yes" AND t.bmi BETWEEN 25 AND 30;




