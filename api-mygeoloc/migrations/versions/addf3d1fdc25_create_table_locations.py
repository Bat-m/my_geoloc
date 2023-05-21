"""Create table locations

Revision ID: addf3d1fdc25
Revises: 
Create Date: 2023-05-21 17:18:52.625300

"""
from alembic import op
import sqlalchemy as sa
import uuid

# revision identifiers, used by Alembic.
revision = 'addf3d1fdc25'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    #création de la table locations
    op.create_table(
        'locations',
        sa.Column('id',sa.UUID(),nullable=False,default=str(uuid.uuid4())),
        sa.Column('trip_time',sa.DateTime(),nullable=True),
        sa.Column('start_location',sa.DateTime(),nullable=False),
        sa.Column('end_location',sa.DateTime(),nullable=True),
        sa.Column('latitude',sa.Float(),nullable=False),
        sa.Column('longitude',sa.Float(),nullable=False),
        sa.Column('accuracy',sa.Float(),nullable=True),
        sa.Column('altitude',sa.Float(),nullable=True),
        sa.Column('accuracy_altitude',sa.Float(),nullable=True),
        sa.Column('speed',sa.Float(),nullable=False),
        sa.Column('heading',sa.Float(),nullable=True),
        sa.PrimaryKeyConstraint('id')
    )


def downgrade() -> None:
    #Suppression de la table locations
    op.drop_table('locations')

