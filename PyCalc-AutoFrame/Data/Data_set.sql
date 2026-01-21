CREATE DATABASE  Cal;
USE Cal;
CREATE TABLE calculator_databse (
    id INT AUTO_INCREMENT PRIMARY KEY,
    n1 DECIMAL(10, 2) NOT NULL,
    n2 DECIMAL(10, 2) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
INSERT INTO calculator_databse (n1, n2) VALUES 
(10.5, 5.0),    -- Row 1
(23, 355),      -- Row 2
(6252, -772),   -- Row 3
(-212, 576),    -- Row 4
(0, 45.5),      -- Row 5
(100.1, 200.2), -- Row 6
(-50, -50),     -- Row 7
(1234, 5678),   -- Row 8
(9.99, 0.01),   -- Row 9
(42, 42);       -- Row 10
select * from  calculator_databse;