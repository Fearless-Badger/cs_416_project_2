START TRANSACTION;

USE user_database;

-- Calculate your student id with (STUDENT_ID - 24)
--       1 <= student_id <= 10
-- Insert through the web-app, not in sql

INSERT INTO user_data (fname, mname, lname, score, student_id)
VALUES
("Micah", "Hunter", "Najacht", 97, 10)
ON DUPLICATE KEY UPDATE
fname=fname,
mname=mname,
lname=lname,
score=score
;

COMMIT;
