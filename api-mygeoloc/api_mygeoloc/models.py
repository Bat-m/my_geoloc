import sqlalchemy as sa
from sqlalchemy.orm import declarative_base, relationship
from flask_login import UserMixin
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import text
from werkzeug.security import check_password_hash, generate_password_hash
Base = declarative_base()

class User(UserMixin,Base):
    __tablename__ = 'users'

    id = sa.Column(UUID(as_uuid=True), server_default=text('gen_random_uuid()'), primary_key=True)
    username = sa.Column(sa.String(50))
    password = sa.Column(sa.String(100))
    email = sa.Column(sa.String(100))


    def to_dict(self):
        return {
            'id': str(self.id),
            'username': self.username,
            'password': self.password,
            'email': self.password,
            'verify_password':self.verify_password
        }
    
    def generate_password(pwd):
            return generate_password_hash( pwd,  method='scrypt')

    def verify_password(self, pwd):
            return check_password_hash(self.password, pwd)