import sqlalchemy as sa
from sqlalchemy.orm import declarative_base, relationship
from flask_login import UserMixin
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import text
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
            'email': self.password
        }
    

