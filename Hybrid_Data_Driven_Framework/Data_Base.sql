-- 1. Create the database
CREATE DATABASE IF NOT EXISTS data_1;
USE data_1;

CREATE TABLE  input (id INT PRIMARY KEY,description VARCHAR(255) );
INSERT INTO input (id, description) VALUES (123, 'Test Data for Selenium');
SELECT * FROM input;
