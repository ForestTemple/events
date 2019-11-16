/*
INSERT INTO Users (email, name, hash, salt) VALUES
	('mike@knights.ucf.edu', 'Michael', '293481-59121sdfasf', 'asd2344234423'),
	('don@knights.ucf.edu', 'Donovan', '293481-1sdfasf', 'as4234423'),
	('seth@ucla.edu', 'Seth', '123492334222342423', '12342134123')
;


INSERT INTO SuperAdmins (uid) VALUES
	(1)

INSERT INTO Admins (uid) VALUES
	(2)

*/

INSERT INTO Locations (latitude, longitude, name) VALUES
	(7.2323, 234.4342, 'UCF Walled Garden')
;

INSERT INTO Universities (name, description, lid, num_students) VALUES
	('The University of Central Florida', 'A great school with a great price.', 1, 50000),
	('The University of UCLA', 'Student debt and more.', 1, 60000),
	('The University of Hunter-Gatherers', 'We do not hunt our own.', 1, 150)
;

INSERT INTO Events (unid, name, description, lid, email, phone, datestamp) VALUES
	(1, 'Chicken Event!', 'There will be birds', 1, 'mike@knights.ucf.edu', '561-606-5434', '20191231T153532'),
	(1, 'Chicken Event 2!', 'There will be more birds', 1, 'mike@knights.ucf.edu', '561-606-5434', '20191231T153532'),
	(2, 'Dog Event!', 'There will be dog', 1, 'mike@knights.ucf.edu', '561-606-5434', '20191231T153532'),
	(3, 'Lizard Event!', 'There will be lizards', 1, 'mike@knights.ucf.edu', '561-606-5434', '20191231T153532')
;

INSERT INTO Events_Private (eid) VALUES
	(1)
;

INSERT INTO Comments (email, text, honor, eid, datestamp) VALUES
	('mike@knights.ucf.edu', 'Hi this is a PRIVATE comment.', '5', '1', '20191125'),
	('mike@knights.ucf.edu', 'Hi this is a comment.', '5', '2', '20191125T1535')
;

INSERT INTO Universities_Pictures (file_path) VALUES
	('/home/mike/Desktop/q.png')
;
