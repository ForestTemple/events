from flask import Flask, render_template, request, flash, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)      
app.secret_key = 'XYZ' # Make me more secret.
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql+psycopg2://events:events@localhost/events"
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
    location = db.relationship(
            'Events_Locations', backref='events', lazy=True, uselist=False)

    def __init__(self, eid, email, name, description, datestamp):
        self.eid = eid
        self.email = email
        self.name = name
        self.description = description
        self.datestamp = datestamp

    def __repr__(self):
        return '<Event "{}: {}">'.format(self.eid, self.name)

class Admins(db.Model):
    uid = db.Column('uid', db.Integer, primary_key = True)

    def __init__(self, uid):
        self.uid = uid

    def __repr__(self):
        return '<Admin "{}">'.format(self.uid)

class SuperAdmins(db.Model):
    uid = db.Column('uid', db.Integer, primary_key = True)

    def __init__(self, uid):
        self.uid = uid

    def __repr__(self):
        return '<SuperAdmin "{}">'.format(self.uid)

class RSOs(db.Model):
    rid = db.Column('rid', db.Integer, primary_key=True)
    name = db.Column('name', db.String(88), nullable=False)

    def __init__(self, rid, name):
        self.rid = rid
        self.name = name

    def __repr__(self):
        return '<RSO "{}">'.format(self.name)

class Events_Private(db.Model):
    eid = db.Column('eid', db.Integer, primary_key=True)

    def __init__(self, eid):
        self.eid = eid

    def __repr__(self):
        return '<EventsPrivate "{}">'.format(self.eid)

class Events_RSO(db.Model):
    eid = db.Column('eid', db.Integer, primary_key=True)
    rid = db.Column('rid', db.Integer, nullable=False)

    def __init__(self, eid, rid):
        self.eid = eid
        self.rid = rid

    def __repr__(self):
        return '<EventsPrivate "{}">'.format(self.eid)

class Comments(db.Model):
    cid = db.Column('cid', db.Integer, primary_key=True)
    eid = db.Column('eid', db.Integer, nullable=False)
    email = db.Column('email', db.String(88), nullable=False)
    text = db.Column('text', db.String(88), nullable=False)
    honor = db.Column('honor', db.Integer)
    datestamp = db.Column('datestamp', db.DateTime)

    def __init__(self, cid, eid, email, text, honor, datestamp):
        self.cid = cid
        self.eid = eid
        self.email = email
        self.text = text
        self.honor = honor
        self.datestamp = datestamp

    def __repr__(self):
        return '<Comment (cid={}, eid={}, email="{}")>'.format(
                self.cid, self.eid, self.email)

class Universities(db.Model):
    unid = db.Column('unid', db.Integer, primary_key=True)
    num_students = db.Column('num_students', db.Integer)
    name = db.Column('name', db.String(88), nullable=False)
    description = db.Column('description', db.String(200))

    def __init__(self, unid, num_students, name, description):
        self.unid = unid
        self.num_students = num_students
        self.name = name
        self.description = description

    def __repr__(self):
        return '<University "{}">'.format(self.name)

class Universities_Pictures(db.Model):
    unid = db.Column('unid', db.Integer)
    file_path = db.Column('file_path', db.String(50), primary_key=True)

    def __init__(self, unid, file_path):
        self.unid = unid
        self.file_path = file_path

    def __repr__(self):
        return '<UniversitiesPictures "{}">'.format(self.file_path)

class Locations(db.Model):
    lid = db.Column('lid', db.Integer, primary_key=True)
    latitude = db.Column('latitude', db.Float, nullable=False)
    longitude = db.Column('longitude', db.Float, nullable=False)
    name = db.Column('name', db.String(88))

    def __init__(self, lid, latitude, longitude, name):
        self.lid = lid
        self.latitude = latitude
        self.longitude = longitude
        self.name = name

    def __repr__(self):
        return '<Location (lat={}, lon={}, name="{}")>'.format(
                self.latitude, self.longitude, self.name)

class Universities_Locations(db.Model):
    lid = db.Column('lid', db.Integer, primary_key=True)
    unid = db.Column('unid', db.Integer, nullable=False)

    def __init__(self, lid, unid):
            self.lid = lid
            self.unid = unid
     
    def __repr__(self):
        return '<UniversityLocation (lid={}, unid={})>'.format(
                self.lid, self.unid)

class Events_Locations(db.Model):
    lid = db.Column('lid', db.Integer, 
            db.ForeignKey('locations.lid'), primary_key=True)
    eid = db.Column('eid', db.Integer,
            db.ForeignKey('events.eid'), nullable=False)

    def __init__(self, lid, eid):
            self.lid = lid
            self.eid = eid
     
    def __repr__(self):
        return '<EventsLocation (lid={}, eid={})>'.format(
                self.lid, self.eid)

@app.route('/')
def home():
  return render_template('home.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        if isValidLogin(request.form['email'], request.form['password']):
            # WTForm
            return redirect(url_for('search'))
        return 

    else:
        return render_template('login.html')

@app.route('/search', methods=['GET', 'POST'])
def search():
    return render_template('search.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    return render_template('signup.html')

if __name__ == '__main__':
  app.run(debug=True)
