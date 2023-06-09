"""Create table user et user-sessions

Revision ID: 05c79710bec8
Revises: addf3d1fdc25
Create Date: 2023-05-21 20:56:05.966843

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '05c79710bec8'
down_revision = 'addf3d1fdc25'
branch_labels = None
depends_on = None


"""Révision Alembic pour le système de connexion et de compte"""

from alembic import op
import sqlalchemy as sa
import uuid


# Révision initiale
def upgrade():
    # Création de la table User
    op.create_table(
        'users',
        sa.Column('id', sa.UUID(), primary_key=True,  default=uuid.uuid4, server_default=sa.text('gen_random_uuid()')),
        sa.Column('email', sa.String(length=255), nullable=False),
        sa.Column('username', sa.String(length=255), nullable=False),
        sa.Column('password', sa.String(length=255), nullable=False),
    )

    op.execute("""
        ALTER TABLE users
        ADD CONSTRAINT check_email_format CHECK (email ~* '^[A-Za-z0-9._+%-]+@[A-Za-z0-9.-]+[.][A-Za-z]+$')
    """)

    # Création de la table UserSession
    op.create_table(
        'user_session',
        sa.Column('id', sa.UUID(), primary_key=True,default=str(uuid.uuid4()), server_default=sa.text('gen_random_uuid()')),
        sa.Column('user_id', sa.UUID(), sa.ForeignKey('users.id'), nullable=False, default=str(uuid.uuid4())),
        sa.Column('session_token', sa.String(length=255), nullable=False),
    )


# Révision inverse
def downgrade():
    # Suppression de la table UserSession
    op.drop_table('user_session')
    op.drop_constraint('check_email_format', 'users', type_='check')
    # Suppression de la table User
    op.drop_table('users')

