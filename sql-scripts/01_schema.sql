START TRANSACTION;

CREATE DATABASE IF NOT EXISTS user_database;

USE user_database;

CREATE TABLE IF NOT EXISTS user_data (
	fname VARCHAR(20),
	mname VARCHAR(20),
	lname VARCHAR(20),
	score INT,
	student_id INT PRIMARY KEY,
	CHECK (student_id >= 1 AND student_id <= 10)
);

COMMIT;
