CREATE TABLE aggregated_transaction (
    id INT AUTO_INCREMENT PRIMARY KEY,
    state VARCHAR(100),
    year INT,
    quarter INT,
    transaction_type VARCHAR(100),
    count BIGINT,
    amount DOUBLE
);

CREATE TABLE aggregated_user (
    id INT AUTO_INCREMENT PRIMARY KEY,
    state VARCHAR(100),
    year INT,
    quarter INT,
    brand VARCHAR(100),
    count BIGINT,
    percentage DOUBLE
);

CREATE TABLE aggregated_insurance (
    id INT AUTO_INCREMENT PRIMARY KEY,
    state VARCHAR(100),
    year INT,
    quarter INT,
    insurance_type VARCHAR(100),
    count BIGINT,
    amount DOUBLE
);

CREATE TABLE map_user (
    id INT AUTO_INCREMENT PRIMARY KEY,
    state VARCHAR(100),
    district VARCHAR(100),
    year INT,
    quarter INT,
    registered_users BIGINT,
    app_opens BIGINT
);

CREATE TABLE map_map (
    id INT AUTO_INCREMENT PRIMARY KEY,
    state VARCHAR(100),
    district VARCHAR(100),
    year INT,
    quarter INT,
    count BIGINT,
    amount DOUBLE
);

CREATE TABLE map_insurance (
    id INT AUTO_INCREMENT PRIMARY KEY,
    state VARCHAR(100),
    district VARCHAR(100),
    year INT,
    quarter INT,
    count BIGINT,
    amount DOUBLE
);

CREATE TABLE top_user (
    id INT AUTO_INCREMENT PRIMARY KEY,
    state VARCHAR(100),
    pincode VARCHAR(20),
    year INT,
    quarter INT,
    registered_users BIGINT
);

CREATE TABLE top_map (
    id INT AUTO_INCREMENT PRIMARY KEY,
    state VARCHAR(100),
    district VARCHAR(100),
    pincode VARCHAR(20),
    year INT,
    quarter INT,
    count BIGINT,
    amount DOUBLE
);

CREATE TABLE top_insurance (
    id INT AUTO_INCREMENT PRIMARY KEY,
    state VARCHAR(100),
    district VARCHAR(100),
    pincode VARCHAR(20),
    year INT,
    quarter INT,
    count BIGINT,
    amount DOUBLE
);
SELECT state, ROUND(SUM(amount),2) AS total_amount
FROM aggregated_transaction
GROUP BY state
ORDER BY total_amount DESC
LIMIT 10;

SELECT transaction_type, ROUND(SUM(amount),2) AS total
FROM aggregated_transaction
GROUP BY transaction_type
ORDER BY total DESC;

SELECT year, ROUND(SUM(amount),2) AS total
FROM aggregated_transaction
GROUP BY year
ORDER BY year;

SELECT state, SUM(count) AS transactions
FROM aggregated_transaction
GROUP BY state
ORDER BY transactions DESC
LIMIT 10;

SELECT state, SUM(amount) total
FROM aggregated_transaction
GROUP BY state
ORDER BY total DESC
LIMIT 10;

SELECT transaction_type, SUM(amount) total
FROM aggregated_transaction
GROUP BY transaction_type
ORDER BY total DESC;

SELECT year, SUM(amount) total
FROM aggregated_transaction
GROUP BY year;

SELECT state, SUM(count) transactions
FROM aggregated_transaction
GROUP BY state
ORDER BY transactions DESC
LIMIT 10;

SELECT year, state, SUM(amount) total
FROM aggregated_transaction
GROUP BY year, state
ORDER BY year, total DESC;