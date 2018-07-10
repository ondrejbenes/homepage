"""IpInfo redefined

Revision ID: eed2a6cbac96
Revises: 
Create Date: 2018-07-10 21:30:50.930805

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'eed2a6cbac96'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('ip_info',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('country', sa.String(length=200), nullable=True),
        sa.Column('city', sa.String(length=200), nullable=True),
        sa.Column('zip', sa.String(length=10), nullable=True),
        sa.Column('lat', sa.Float(), nullable=True),
        sa.Column('lon', sa.Float(), nullable=True),
        sa.Column('timezone', sa.String(length=20), nullable=True),
        sa.Column('datetime', sa.DateTime(), nullable=True),
        sa.PrimaryKeyConstraint('id')
    )


def downgrade():
    op.drop_table('ip_info')
