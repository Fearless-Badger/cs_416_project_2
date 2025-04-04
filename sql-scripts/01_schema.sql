START TRANSACTION;

CREATE DATABASE IF NOT EXISTS user_database;

USE user_database;

CREATE TABLE IF NOT EXISTS user_data (
	fname VARCHAR(32),
	mname VARCHAR(32),
	lname VARCHAR(32),
	score INT,
	student_id INT PRIMARY KEY,
	CHECK (student_id >= 1 AND student_id <= 10)
);

COMMIT;
