from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy(app)

class Users(db.Model):
    uid = db.Column('uid', db.Integer, primary_key = True)
    email = db.Column('email', db.String(30), unique=True, nullable=False)
    name = db.Column('name', db.String(30), nullable=False)
    hashed = db.Column('hash', db.String(512), nullable=False)
    salt = db.Column('salt', db.String(512), nullable=False)

    def __init__(self, uid, email, name, hashed, salt):
        self.uid = uid
        self.email = email
        self.name = name
        self.hashed = hashed
        self.salt = salt

    def __repr__(self):
        return '<User "{}">'.format(self.email)

class Events(db.Model):
    eid = db.Column('eid', db.Integer, primary_key = True)
    email = db.Column('email', db.String(30), nullable=False)
    name = db.Column('name', db.String(88), nullable=False)
    description = db.Column('description', db.String(88))
    datestamp = db.Column('datestamp', db.DateTime, nullable=False)
    # here

    def __init__(self, eid, email, name, description, datestamp):
        self.eid = eid
        self.email = email
        self.name = name
        self.description = description
        self.datestamp = datestamp

    def __repr__(self):
        return '<Event "{}: {}">'.format(self.eid, self.name)
