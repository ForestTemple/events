INSERT INTO Locations (latitude, longitude, name) VALUES
	(28.538336, -81.379234, 'UCF'),
	(28.538337, -81.379235, 'UCLA'),
	(28.538338, -81.379236, 'UHG'),
	(28.538339, -81.379237, 'UCF Walled Garden'),
	(28.538330, -81.379238, 'UCLA Gene Pool'),
	(28.538331, -81.379239, 'UCF Biology Building'),
	(28.538332, -81.379230, 'Ancestral Hunting Grounds'),
	(28.538333, -81.379231, 'UCF Underground Tunnels')
;

INSERT INTO Universities (name, description, lid, num_students) VALUES
	('The University of Central Florida', 'A great school with a great price.', 1, 50000),
	('The University of UCLA', 'Student debt and more.', 2, 60000),
	('The University of Hunter-Gatherers', 'We do not hunt our own.', 3, 150)
;

/* password for all is: welcome */
INSERT INTO Users (unid, email, name, hash, salt) VALUES
   (1, 'mike@knights.ucf.edu', 'Michael S', 'pbkdf2:sha256:150000$PWArbloj$32eada7dc35d8c8aa5a0908c8ed50ab2b0e8261ca10432ae6389036b7f2d62af', 'mMvzfT1_s35JRa4qKMzXOtEjoxRD5I9HAYu7v2cHo6k'),
   (2, 'ash@ucla.edu', 'Ash', 'pbkdf2:sha256:150000$EoNsz8Ac$bc35a9823345ab62ca21c34e0322064ca1e0c9824633fdbbd0fb9a260efd84ea', 'VUwAeBx6qoJR9S7bcr1Z7wR8BntUWpKfeufRWhbC5dE'),
   (3, 'brent@hunters.edu', 'Brent', 'pbkdf2:sha256:150000$96bPMIB3$8df9b8e23ab999b9469d0a5df213b24c4f4535adff95d7327645c6520117a802', 'KDR16a2Nq3YdtX3VzN1wrH3X0F2agCPDJbJjD5g_-78')
;

INSERT INTO Super_Admins (uid) VALUES
	(1)
;

INSERT INTO RSOs (name) VALUES
	('Hunter Runes')
;

INSERT INTO Admins (uid, rid) VALUES
	(3, 1)
;

INSERT INTO Events (unid, name, description, lid, email, phone, datestamp) VALUES
	(1, 'Chicken Event!', 'There will be birds', 1, 'mike@knights.ucf.edu', '561-606-5434', '20191231T153532'),
	(1, 'Chicken Event 2!', 'There will be more birds', 2, 'don@ucla.edu', '561-606-5434', '20191231T153532'),
	(2, 'Dog Event!', 'There will be dog', 1, 'vv@knights.ucf.edu', '561-606-5434', '20191231T153532'),
	(3, 'Lizard Event!', 'There will be lizards', 4, 'mike@knights.ucf.edu', '561-606-5434', '20191231T153532'),
	(3, 'Secret Vulture Event.', 'Bring corpses...', 5, 'vulture@hunters.edu', '234-234-2342', '20180909T090909')
;

INSERT INTO Events_Private (eid) VALUES
	(1)
;

INSERT INTO Comments (eid, uid, text, rating, datestamp) VALUES
	(1, 1, 'This was a great chicken event!', 5, '20190909T090909'),
	(2, 1, 'This was another great chicken event!', 4, '20190909T090909'),
	(3, 1, 'This was an unrelated dog event.', 3, '20190909T090909')
;

INSERT INTO Universities_Pictures (unid, file_path) VALUES
	(1, '/home/mike/Desktop/q.png')
;
