START TRANSACTION;

USE user_database;

INSERT INTO user_data (fname, mname, lname, score, student_id)
VALUES
("Micah", "Hunter", "Najacht", 100, 10),
('Mauricio', 'Smith', 'Herrera', 70, 9),
('Mason', 'Ant', 'Elizondo', 35, 8),
('Luis', 'David', 'Contreras', 45, 7 ),
('Lorial', 'Marie', 'Lesniewski', 0, 6),
('Lolia', 'Kalada', 'Halliday', 90, 5),
('Leonardo', 'The-Kid', 'Zavala', 85, 4),
('Lazar', 'The-Guy', 'Stanisavljevic', 97, 3),
('Justin', 'Taylor', 'Brent', 70, 2),
('Jesse', 'Christ', 'Trejo', 90, 1)
ON DUPLICATE KEY UPDATE
fname=fname,
mname=mname,
lname=lname,
score=score
;

COMMIT;
