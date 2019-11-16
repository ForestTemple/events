import secrets

from flask import Flask, render_template, request, flash, redirect, url_for, sessions

from werkzeug.security import generate_password_hash, check_password_hash

from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField
from wtforms.fields.html5 import DateField
from wtforms.validators import DataRequired, Email, Length

from flask_login import LoginManager, UserMixin, current_user, login_user, logout_user

app = Flask(__name__)      
app.secret_key = 'My very first predatory hawk scooped their prey off the palm tree in my garden yesterday morning at 10AM sharp.'
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql+psycopg2://events:events@localhost/events"
db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.init_app(app)

class RSOCreateForm(FlaskForm):
    name = StringField('Event Name', validators=[DataRequired(), Length(4, 50)])
    university = SelectField(
            'University', 
            choices = [('impl', "Implement me")]
    )
    email1 = StringField('email1', validators=[DataRequired(), Email(), Length(4, 50)])
    email2 = StringField('email2', validators=[DataRequired(), Email(), Length(4, 50)])
    email3 = StringField('email3', validators=[DataRequired(), Email(), Length(4, 50)])
    email4 = StringField('email4', validators=[DataRequired(), Email(), Length(4, 50)])
    email5 = StringField('email5', validators=[DataRequired(), Email(), Length(4, 50)])
    submit = SubmitField('Create')

class SearchForm(FlaskForm):
    # Event name: Text
    # Event type: Drop-down {Public, Private, RSO} ONLY AUTHENTICATED
    # University: Text  # nickname table for uni?
    # Date: DatePicker.html
    event_name = StringField('Event Name', validators=[Length(0, 500)])
    event_type = SelectField(
            'Event Type',
            choices = [('all', 'All Events'), ('public', 'Public Events'), ('private', 'Private Events'), ('rso', 'RSO Events')]
    )
    university_name = StringField('University Name', validators=[Length(0, 500)])
    date_from = DateField('From:', format='%Y-%m-%d', validators=[])
    date_to = DateField('To:', format='%Y-%m-%d', validators=[])
    submit = SubmitField('Search!')

class LoginForm(FlaskForm):
    email = StringField('email', validators=[DataRequired(), Email(), Length(4, 50)])
    password = PasswordField('password', validators=[DataRequired(), Length(6, 50)])
    login = SubmitField()

class SignupForm(FlaskForm): # TODO When a form goes bad, it doesn't tell you what field is wrong.
    email = StringField('email', validators=[DataRequired(), Email(), Length(4, 50)])
    name = StringField('name', validators=[DataRequired(), Length(1, 20)])
    password = PasswordField('password', validators=[DataRequired(), Length(6, 50)])
    signup = SubmitField()

class Users(db.Model, UserMixin):
    uid = db.Column('uid', db.Integer, primary_key = True)
    email = db.Column('email', db.String(50), unique=True, nullable=False)
    name = db.Column('name', db.String(50))
    salt = db.Column('salt', db.String(32), nullable=False)
    hashed = db.Column('hash', db.String(256), nullable=False)

    def __init__(self, email, name, password):
        self.email = email
        self.name = name
        self.salt = secrets.token_urlsafe(32) # Columns are too large for hash and salt?
        self.set_password(password)

    def set_password(self, password):
        self.hashed = generate_password_hash(password + self.salt)

    def check_password(self, password):
        return check_password_hash(self.hashed, password + self.salt)

    def get_id(self):
        return self.uid

    def __repr__(self):
        return '<User "{}">'.format(self.email)

class Events(db.Model):
    eid = db.Column('eid', db.Integer, primary_key = True)
    email = db.Column('email', db.String(50), nullable=False)
    name = db.Column('name', db.String(100), nullable=False)
    description = db.Column('description', db.String(100))
    lid = db.Column('lid', db.ForeignKey('locations.lid'), nullable=False)
    datestamp = db.Column('datestamp', db.DateTime, nullable=False)

    def __init__(self, eid, email, name, description, datestamp):
        self.eid = eid
        self.email = email
        self.name = name
        self.description = description
        self.datestamp = datestamp

    def __repr__(self):
        return '<Event "{}: {}">'.format(self.eid, self.name)


# collapse me to simple integer type in Users
class Admins(db.Model):
    uid = db.Column('uid', db.Integer, db.ForeignKey('users.uid'), primary_key = True)

    def __init__(self, uid):
        self.uid = uid

    def __repr__(self):
        return '<Admin "{}">'.format(self.uid)

# collapse me to simple integer type in Users
class SuperAdmins(db.Model):
    uid = db.Column('uid', db.Integer, db.ForeignKey('users.uid'), primary_key = True)

    def __init__(self, uid):
        self.uid = uid

    def __repr__(self):
        return '<SuperAdmin "{}">'.format(self.uid)

class RSOs(db.Model):
    rid = db.Column('rid', db.Integer, primary_key=True)
    uid = db.Column('uid', db.Integer, db.ForeignKey('users.uid'), nullable=False)
    name = db.Column('name', db.String(100), nullable=False)

    def __init__(self, uid, name):
        self.uid = uid
        self.name = name

    def __repr__(self):
        return '<RSO "{}">'.format(self.name)

class EventsPrivate(db.Model):
    eid = db.Column('eid', db.Integer, primary_key=True)

    def __init__(self, eid):
        self.eid = eid

    def __repr__(self):
        return '<EventsPrivate ({})>'.format(self.eid)

class EventsRSO(db.Model):
    eid = db.Column('eid', db.Integer, db.ForeignKey('events.eid'), primary_key=True)
    rid = db.Column('rid', db.Integer, db.ForeignKey('rsos.rid'), nullable=False)

    __tablename__ = "events_rso"

    def __init__(self, eid, rid):
        self.eid = eid
        self.rid = rid

    def __repr__(self):
        return '<EventsPrivate ({}, {})>'.format(self.eid, self.rid)

class RSOs_Member(db.Model):
    rid = db.Column('rid', db.Integer, db.ForeignKey('rsos.rid'), primary_key=True)
    uid = db.Column('uid', db.Integer, 
            db.ForeignKey('users.eid'), primary_key=True, nullable=False)

    def __init__(self, rid, uid):
        self.rid = rid
        self.uid = uid

    def __repr__(self):
        return '<RSOMember (rid={}, uid={})>'.format(self.rid, self.uid)

class Comments(db.Model):
    cid = db.Column('cid', db.Integer, primary_key=True)
    eid = db.Column('eid', db.Integer, nullable=False)
    email = db.Column('email', db.String(100), nullable=False)
    text = db.Column('text', db.String(100), nullable=False)
    honor = db.Column('honor', db.Integer)
    datestamp = db.Column('datestamp', db.DateTime)

    def __init__(self, eid, email, text, honor, datestamp):
        self.eid = eid
        self.email = email
        self.text = text
        self.honor = honor
        self.datestamp = datestamp

    def __repr__(self):
        return '<Comment (eid={}, email="{}")>'.format(
                self.eid, self.email)

class Universities(db.Model):
    unid = db.Column('unid', db.Integer, primary_key=True)
    name = db.Column('name', db.String(100), nullable=False)
    description = db.Column('description', db.String(200))
    lid = db.Column('lid', db.Integer, db.ForeignKey('locations.lid'), nullable=False) # update me
    num_students = db.Column('num_students', db.Integer)

    def __init__(self, unid, name, description, lid, num_students):
        self.unid = unid
        self.name = name
        self.description = description
        self.lid = lid
        self.num_students = num_students

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
    name = db.Column('name', db.String(100))

    def __init__(self, lid, latitude, longitude, name):
        self.lid = lid
        self.latitude = latitude
        self.longitude = longitude
        self.name = name

    def __repr__(self):
        return '<Location (lat={}, lon={}, name="{}")>'.format(
                self.latitude, self.longitude, self.name)

@login_manager.user_loader
def load_user(uid):
    return Users.query.get(int(uid))

@app.route('/')
def home():
    if current_user.is_authenticated:
        return redirect(url_for('search'))
    return render_template('home.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('search'))

    form = LoginForm()
    if form.validate_on_submit():
        user = Users.query.filter_by(email=form.email.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user)
        cuid = current_user.get_id()
        current_user.is_superadmin = \
            SuperAdmins.query.filter_by(uid=cuid).first() is not None
        current_user.is_admin = \
            Admins.query.filter_by(uid=cuid).first() is not None
        return redirect(url_for('search'))
    else:
        print("not valid")
        print(form.email.data, form.password.data)
        return render_template('login.html', form=form)

@app.route('/logout')
def logout():
    current_user.admin = False
    current_user.superadmin = False 
    logout_user()
    return redirect(url_for('home'))

@app.route('/profile', methods=['GET', 'POST'])
def profile():
    if current_user.is_anonymous:
        return redirect(url_for('login'))

    if current_user.is_superadmin:
        print("superadmin")
    elif current_user.is_admin:
        print("admin")
    else: 
        print("autheduser")

@app.route('/rso/create', methods=['GET', 'POST'])
def rso_create():
    if current_user.is_anonymous:
        return redirect(url_for('login'))

    form = RSOCreateForm()
    if form.validate_on_submit():
        name = form.name.data
        emails = [
                form.email1.data, form.email2.data,
                form.email3.data, form.email4.data,
                form.email5.data
        ]
        for email in emails:
            if Users.query.filter_by(email=email).first() is None:
                flash('Email "{}" is not signed up.'.format(email))
                return redirect(url_for('rso_create'))
        if RSOs.query.filter_by(name=name).first() is not None:
                flash('That name is already taken.')
                return redirect(url_for('rso_create'))

        db.session.add(RSOs(current_user.get_id(), name))
        db.session.commit()
        for email in emails:
            db.session.add(
                RSOs_Member(RSOs.query.filter_by(name=name), 
                Users.query.filter_by(email=email).first().uid)
            )
        db.session.commit()
        return redirect(url_for('rso_manage'))
    return render_template('rso/create.html', form=form)

@app.route('/rso/manage', methods=['GET', 'POST'])
def rso_manage():
    return render_template('rso/manage.html')

@app.route('/university/create', methods=['GET', 'POST'])
def university_create():
    return render_template('university/create.html')

@app.route('/university/manage', methods=['GET', 'POST'])
def university_manage():
    return render_template('university/manage.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if current_user.is_authenticated:
        return redirect(url_for('search'))

    form = SignupForm()
    if form.validate_on_submit():
        print(' '.join([form.email.data, form.name.data, form.password.data]))
        user = Users.query.filter_by(email=form.email.data).first()
        if user:
            flash('This email is already taken.')
            print("Taken user: " + str(user))
            return redirect(url_for('signup'))
        new_user = Users(form.email.data, form.name.data, form.password.data)
        db.session.add(new_user)
        db.session.commit()
        login_user(new_user)
        return redirect(url_for('search'))
    return render_template('signup.html', form=form)

@app.route('/search', methods=['GET', 'POST'])
def search():
    form = SearchForm()
    items = []
    print('validating')
    if form.validate_on_submit():
        if form.event_type.data == 'public':
            events = Events.query.all()
            for e in events:
                if EventsPrivate.query.filter_by(eid=e.eid).first() is None \
                        and EventsRSO.query.filter_by(eid=e.eid).first() is None:
                    items.append(e)
        elif form.event_type.data == 'private':
            private_events = EventsPrivate.query.all()
            for p in private_events:
                event = Events.query.filter_by(eid=p.eid).first()
                if event is not None:
                    items.append(event)
        elif form.event_type.data == 'rso':
            rso_events = EventsRSO.query.all()
            for r in rso_events:
                event = Events.query.filter_by(eid=r.eid).first()
                if event is not None:
                    items.append(event)
        else: # All events.
            items = Events.query.limit(10).all()

    print('this was a ' + form.event_type.data) 
    print("items: " + str(items))
    return render_template('search.html', form=form, items=items)

if __name__ == '__main__':
  app.run(debug=True)
