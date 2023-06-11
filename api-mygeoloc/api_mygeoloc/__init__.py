
from api_mygeoloc.db import session
from api_mygeoloc.models import User
import flask, flask_login

from .auth import auth as auth_blueprint
from .main import main as main_blueprint
from dotenv import load_dotenv

import os

# Charger les variables d'environnement à partir du fichier .env
load_dotenv()

# Accéder à la valeur d'une variable d'environnement
secret_key = os.getenv('SECRET_KEY') or os.urandom(24)

app = flask.Flask(__name__)
app.secret_key = secret_key 


login_manager = flask_login.LoginManager()
login_manager.login_view = 'auth.login'
login_manager.init_app(app)



# Exemple d'utilisation : obtenir tous les utilisateurs de la table "users"

users = session.query(User).all()
for user in users:
        print(f"User ID: {user.id}, Username: {user.username}")
# N'oubliez pas de fermer la session après utilisation
#session.close()

def check_user(email):
    user=session.query(User).filter_by(email=email).first()
    if user:  
        return user
    else:
        return None

@login_manager.user_loader
def user_loader(email):
    return check_user(email)

@login_manager.request_loader
def request_loader(request):
    email = request.form.get('email')
    if email not in users:
        return

    user = User()
    user.id = email
    return user

# blueprint for auth routes in our app
app.register_blueprint(auth_blueprint)

# blueprint for non-auth parts of app
app.register_blueprint(main_blueprint)

# run app
app.run(debug=True)

