from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import sqlalchemy as sa
from flask_login import LoginManager, login_user, login_required, logout_user, UserMixin
from alembic.config import Config

# Lire l'URL de la base de données depuis le fichier alembic.ini
alembic_config = Config('alembic.ini')
database_url = alembic_config.get_section_option('alembic', 'sqlalchemy.url')

Base = declarative_base()
# Créer un moteur SQLAlchemy
engine = create_engine(database_url)

# Créer une classe Session pour gérer les requêtes
Session = sessionmaker(bind=engine)
session = Session()

# Utiliser la session pour effectuer des opérations sur la base de données
# par exemple, exécuter des requêtes, ajouter ou mettre à jour des enregistrements, etc.
class User(Base):
    __tablename__ = 'user'

    id = sa.Column(sa.UUID(), primary_key=True)
    username = sa.Column(sa.String(50))
    password = sa.Column(sa.String(100))

   
# Exemple d'utilisation : obtenir tous les utilisateurs de la table "users"
users = session.query(User).all()
for user in users:
        print(f"User ID: {user.id}, Username: {user.username}")
# N'oubliez pas de fermer la session après utilisation
session.close()
