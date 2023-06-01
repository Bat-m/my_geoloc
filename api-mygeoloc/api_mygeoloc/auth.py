

from api_mygeoloc.db import session
from api_mygeoloc.models import User
from flask import Blueprint, render_template, redirect, url_for
import flask, flask_login
from werkzeug.security import generate_password_hash, check_password_hash


# Create a session factory

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if flask.request.method == 'GET':
        return render_template('login.html')
    #session_login=initialize_session()
    users = session.query(User).all()
    api_key = str(flask.request.headers.get('Cookie'))
    print('api_key: ',api_key.split("session=",1)[1])
    for user in users:
        if user.email==flask.request.form['email'] and user.verify_password(flask.request.form['password']):
            connected_user = User()
            connected_user.id = user.email
            flask_login.login_user(connected_user, remember=True)
            return redirect(url_for('auth.protected'))

    return 'Bad login'

@auth.route('/protected', methods=['GET'])
@flask_login.login_required
def protected():
    return 'Logged in as: ' + flask_login.current_user.email

@auth.route('/signup')
def signup():
    return render_template('signup.html')


@auth.route('/signup', methods=['POST'])
def signup_post():
  
    email = flask.request.form.get('email')
    username = flask.request.form.get('username')
    password = flask.request.form.get('password')

    user =  session.query(User).filter_by(email=email).first() 
    print("user signup: ",user)
    if user: 
        return redirect(url_for('auth.login'))

    new_user = User(username=username, password=User.generate_password(password),email=email)
    
    session.add(new_user)
    session.commit()
    return redirect(url_for('auth.login'))

@auth.route('/logout')
def logout():
    return 'Logout'