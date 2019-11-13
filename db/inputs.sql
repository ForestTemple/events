INSERT INTO Users (email, name, hash, salt) VALUES
	('mike@knights.ucf.edu', 'Michael', '293481-59121sdfasf', 'asd2344234423'),
	('jojo-kang@knights.ucf.edu', 'jojo', '293481-1sdfasf', 'as4234423')
;

INSERT INTO SuperAdmins (UID) VALUES
	(1)
;

INSERT INTO Events (email, name, description, phone, datestamp) VALUES
	('mike@knights.ucf.edu', 'Michael', 'This is a fun event', '561-545-4324', '20191231T153532')
;

INSERT INTO Universities (num_students, name, description) VALUES
	(150, 'The University of Hunter-Gatherers', 'We hunt our own.')
;

INSERT INTO Universities_Pictures (file_path) VALUES
	('/home/mike/Desktop/q.png')
;
