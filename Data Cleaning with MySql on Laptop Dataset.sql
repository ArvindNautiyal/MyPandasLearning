-- EDA AND CLEANING IN LAPTOP DATASET

USE projects;

-- CREATING BACKUP OF DATABASE

CREATE TABLE laptop LIKE laptop_backup ;

INSERT INTO laptop

SELECT * FROM laptop_backup;

SELECT * FROM laptop;

-- REMOVING UNWANTED COLUMN ex - UNNAMED : 0

ALTER TABLE laptop DROP COLUMN `Unnamed: 0`;

SELECT * FROM laptop;

-- ADDING A NEW COLUMN ID

ALTER TABLE laptop ADD COLUMN Id INT AUTO_INCREMENT PRIMARY KEY AFTER Company;

SELECT * FROM laptop;

-- CLEANING STAGE
-- Removing GB from RAM column ex  - 8GB TO 8

UPDATE laptop
SET Ram = REPLACE(Ram, 'GB', '')
WHERE ID IN (SELECT ID FROM (SELECT ID FROM laptop) AS temp);

SELECT * FROM laptop;

-- Changing dtype of RAM

ALTER TABLE laptop MODIFY Ram INTEGER;


-- CREATING NEW COLUMN GPU NAME AND GPU BRAND

ALTER TABLE laptop ADD COLUMN gpu_brand VARCHAR(255) AFTER Gpu;

ALTER TABLE laptop ADD COLUMN gpu_name VARCHAR(255) AFTER Gpu;

SELECT * FROM laptop;

UPDATE laptop
SET gpu_brand = (SUBSTRING_INDEX(Gpu," ",1))
WHERE Id IN (SELECT Id FROM (SELECT Id FROM laptop) t1);

UPDATE laptop
SET gpu_name = (SUBSTRING_INDEX(Gpu," ",-2))
WHERE Id IN (SELECT Id FROM (SELECT Id FROM laptop) t1);

SELECT * FROM laptop;

-- DROP GPU column 

ALTER TABLE laptop DROP COLUMN Gpu;

SELECT * FROM laptop;


-- UPDATING PRICE 
UPDATE laptop
SET Price = (ROUND(Price))
WHERE Id IN (SELECT Id FROM (SELECT Id FROM laptop) temp);

-- CHANGING DTYPE OF PRICE COLUMN

ALTER TABLE laptop MODIFY Price INTEGER;

SELECT DISTINCT(OpSys) FROM laptop;

-- CHANING Osys
SELECT 
    CASE 
        WHEN OpSys LIKE '%mac%' THEN 'mac'
        WHEN OpSys LIKE '%Windows%' THEN 'windows'
        WHEN OpSys LIKE '%Linux%' THEN 'Linux'
        WHEN OpSys LIKE '%No OS%' THEN 'N/A'
        ELSE 'Others'
    END AS Operating_System
FROM laptop;

UPDATE laptop
SET OpSys = (CASE 
				WHEN OpSys LIKE '%mac%' THEN 'mac'
				WHEN OpSys LIKE '%Windows%' THEN 'windows'
				WHEN OpSys LIKE '%Linux%' THEN 'Linux'
				WHEN OpSys LIKE '%No OS%' THEN 'N/A'
				ELSE 'Others'
			END )
WHERE Id IN (SELECT Id FROM (SELECT Id FROM laptop)t1);

SELECT * FROM laptop;

-- ADDING NEW COLUMN STORAGE AND STORAGE DEVICE

ALTER TABLE laptop ADD COLUMN Storage VARCHAR(255) AFTER Memory;

ALTER TABLE laptop ADD COLUMN Storage_device VARCHAR(255) AFTER Memory;

SELECT * FROM laptop;

UPDATE laptop
SET Storage = ( SUBSTRING_INDEX(Memory," ",1))
WHERE Id IN (SELECT Id FROM (SELECT Id FROM laptop) t);

SELECT * FROM laptop;

UPDATE laptop
SET Storage_device = (SUBSTRING_INDEX(Memory," ",-5)) 
WHERE Id IN (SELECT Id FROM (SELECT Id FROM laptop) t);

-- DROP COLUMN MEMORY

ALTER TABLE laptop DROP COLUMN Memory;

SELECT * FROM laptop;

-- CREATING COLUMN Cpubrand , cpuname , cpuspeed

ALTER TABLE laptop ADD COLUMN cpu_brand VARCHAR(255) AFTER Cpu;

ALTER TABLE laptop ADD COLUMN cpu_name VARCHAR(255) AFTER cpu_brand;

ALTER TABLE laptop ADD COLUMN cpu_speed VARCHAR(255) AFTER cpu_name;

-- UPDATING COLUMNS

UPDATE laptop
SET cpu_speed = (SUBSTRING_INDEX(Cpu," ",-1))
WHERE Id IN (SELECT Id FROM (SELECT Id FROM laptop) t);

UPDATE laptop
SET cpu_brand = (SUBSTRING_INDEX(REPLACE(Cpu,cpu_speed," "), " ",2))
WHERE Id IN (SELECT Id FROM (SELECT Id FROM laptop) t1);

UPDATE laptop
SET cpu_name = ( REPLACE((REPLACE(Cpu,cpu_brand," ")) , cpu_speed ," " ))
WHERE Id IN (SELECT Id FROM (SELECT Id FROM laptop) t1 );

-- DROP Cpu Column

ALTER TABLE laptop DROP COLUMN Cpu;

-- CORRECTING MISTAKE

UPDATE laptop
SET Storage_device = (REPLACE(Storage_device,Storage, " "))
WHERE Id IN (SELECT Id FROM (SELECT Id FROM laptop) t1);

UPDATE laptop
SET Storage_device = (TRIM(Storage_device))
WHERE Id IN (SELECT Id FROM (SELECT Id FROM laptop) t1);

SELECT * FROM laptop;

-- CLEAN cpu_speed Removing GHZ and CHANGING DTYPE

UPDATE laptop
SET cpu_speed = (CAST(REPLACE(cpu_speed,"GHz"," ") AS DECIMAL(10,2) ))
WHERE Id IN (SELECT Id FROM (SELECT Id FROM laptop) t1);

-- CORRECTING WEIGHT AND CHANGING DTYPE

UPDATE laptop
SET Weight = (REPLACE(Weight, "kg" , " ")) 
WHERE Id IN (SELECT Id FROM (SELECT Id FROM laptop) t1);

UPDATE laptop
SET Weight = ROUND(Weight)
WHERE Id IN (SELECT Id FROM (SELECT Id FROM laptop) t1);

ALTER TABLE laptop MODIFY Weight INTEGER;

SELECT * FROM laptop;

-- CREATING SCREEN WIDTH AND SCREEN LENGTH COLUMN

ALTER TABLE laptop ADD COLUMN screen_width INTEGER AFTER ScreenResolution;

ALTER TABLE laptop ADD COLUMN screen_length INTEGER AFTER screen_width ;

SELECT * FROM laptop;

UPDATE laptop
SET screen_length = (SUBSTRING_INDEX(ScreenResolution,"x",-1))
WHERE Id IN (SELECT Id FROM(SELECT Id FROM laptop) t);

ALTER TABLE laptop MODIFY screen_length INTEGER;

SELECT * FROM laptop;

UPDATE laptop
SET screen_width = (REPLACE(SUBSTRING_INDEX(REPLACE(ScreenResolution,screen_length," "), " ", -2 ),"x"," ") )
WHERE Id IN (SELECT Id FROM (SELECT Id FROM laptop) t1);

ALTER TABLE laptop MODIFY screen_width INTEGER;

SELECT * FROM laptop;

-- CREATOING COLUMN TO KNOW WHETHER LAPTOP IS TOUCH SCREEN OR NOT

ALTER TABLE laptop ADD COLUMN TouchScreen INTEGER AFTER Inches;

SELECT * FROM laptop;

UPDATE laptop
SET TouchScreen = (CASE 
						WHEN ScreenResolution LIKE "%Touchscreen%" THEN 1
						ELSE 0
					END );
                    
SELECT * FROM laptop;

-- CLEANING cpu_name

UPDATE laptop
SET cpu_name = (SUBSTRING_INDEx(TRIM(cpu_name)," ",1))
WHERE Id IN (SELECT Id FROM (SELECT Id FROM laptop) t1);

SELECT * FROM laptop;

UPDATE laptop
SET Storage_device = (CASE
						WHEN Storage_device LIKE '%SSD%' AND Storage_device LIKE '%HDD%' THEN 'Hybrid'
						WHEN Storage_device LIKE '%SSD%' THEN 'SSD'
						WHEN Storage_device LIKE'%HDD%' THEN 'HDD'
						WHEN Storage_device LIKE '%Flash Storage%' THEN 'Flash Storage'
						WHEN Storage_device LIKE '%Hybrid%' THEN 'Hybrid'
						WHEN Storage_device LIKE '%Flash Storage%' AND Storage_device LIKE '%HDD%' THEN 'Hybrid'
						ELSE NULL
					END );
SELECT * FROM laptop;










































