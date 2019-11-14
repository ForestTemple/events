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
    # here

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

    def __init__(self, uid, email, name, hashed, salt):
        self.uid = uid

    def __repr__(self):
        return '<Admin "{}">'.format(self.uid)

class RSOs(db.Model):
    rid = db.Column('rid', db.Integer, primary_key=True)
    name = db.Column('name', db.String(88), nullable=False)

    def __init__(self, rid, name):
        self.rid = rid
        self.name = name

    def __repr__(self):
        

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
