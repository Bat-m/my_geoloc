


from api_mygeoloc.db import session
from api_mygeoloc.models import User,User_Session
from flask import Blueprint, render_template, redirect, url_for,current_app
import flask, flask_login
from sqlalchemy import text,insert
from api_mygeoloc.oauthy import oauthI
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
    api_key = str(flask.request.headers.get('Cookie'))
    print('headers: ',flask.request.headers)
    #stmt=insert(User).values(user_id=flask_login.current_user.id,session_token=api_key.split("session=",1)[1])
    session.execute(insert(User_Session),{"user_id":flask_login.current_user.id,"session_token":api_key.split("session=",1)[1]})
    session.commit()
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
    session.close()
    return 'Logout'

#Google part
@auth.route('/log/google')
def login_google():
    redirect_uri = url_for('auth.authorize_google', _external=True)
    return oauthI.google.authorize_redirect(redirect_uri)

@auth.route('/authorize/google')
def authorize_google():
    token = oauthI.google.authorize_access_token()
    print("token google: ",token['userinfo'])
    user_info = token['userinfo']
    #cvérifier si l'utilisateur n'existe pas dans ce cas on le crée
    new_user = User(username=user_info['name'], password=User.generate_password(token['access_token']),email=user_info['email'])
    
    session.add(new_user)
    session.commit()
    return redirect(url_for('main.index'))

@auth.route('/log/out/google')
def logoutGoogle():
    session.close()
    print("logout google", session)
    #check here user in user_sessions
    #session.pop('user', None)
    #oauthI.google.revoke_token(session['google_token'])
    return redirect(url_for('main.index'))