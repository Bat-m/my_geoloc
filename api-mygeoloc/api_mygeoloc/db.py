from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from alembic.config import Config

# Lire l'URL de la base de données depuis le fichier alembic.ini
alembic_config = Config('alembic.ini')
database_url = alembic_config.get_section_option('alembic', 'sqlalchemy.url')

engine = create_engine(database_url)
Session = sessionmaker(bind=engine)
session = Session()