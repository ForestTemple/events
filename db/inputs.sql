/*
INSERT INTO Users (email, name, hash, salt) VALUES
	('mike@knights.ucf.edu', 'Michael', '293481-59121sdfasf', 'asd2344234423'),
	('donovan@knights.ucf.edu', 'Donovan', '293481-1sdfasf', 'as4234423'),
	('seth@ucla.edu', 'Seth', '123492334222342423', '12342134123')
;
*/

/*
INSERT INTO SuperAdmins (uid) VALUES
	(1)
;

INSERT INTO Admins (uid) VALUES
	(2)
;
*/

INSERT INTO Events (email, name, description, phone, datestamp) VALUES
	('mike@knights.ucf.edu', 'Michael', 'This is a fun PRIVATE event', '561-545-4324', '20191231T153532'),
	('mike@knights.ucf.edu', 'Michael', 'This is also a very fun event', '561-545-4324', '20191125T153532')
;

INSERT INTO Events_Private (eid) VALUES
	(1)
;

INSERT INTO Comments (email, text, honor, eid, datestamp) VALUES
	('mike@knights.ucf.edu', 'Hi this is a PRIVATE comment.', '5', '1', '20191125'),
	('mike@knights.ucf.edu', 'Hi this is a comment.', '5', '2', '20191125T1535')
;

INSERT INTO Universities (num_students, name, description) VALUES
	(50000, 'The University of Central Florida', 'A great school with a great price.'),
	(150, 'The University of UCLA', 'Student debt and more.'),
	(60000, 'The University of Hunter-Gatherers', 'We do not hunt our own.')
;

INSERT INTO Locations (latitude, longitude, name) VALUES
	(7.2323, 234.4342, 'UCF Walled Garden')
;

INSERT INTO Universities_Locations (lid, unid) VALUES
	(1, 1)
;

INSERT INTO Events_Locations (lid, eid) VALUES
	(1, 1)
;

INSERT INTO Universities_Pictures (file_path) VALUES
	('/home/mike/Desktop/q.png')
;
