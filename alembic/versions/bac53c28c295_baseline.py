"""baseline

Revision ID: bac53c28c295
Revises: 
Create Date: 2022-03-20 23:41:17.378536

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bac53c28c295'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'users',
        sa.Column('id', sa.Integer, primary_key=True, autoincrement=True),
        sa.Column('username', sa.String(20), unique=True, nullable=False),
        sa.Column('password', sa.String(200), nullable=False),
        sa.Column('name', sa.String(60), nullable=False),
        sa.Column('email', sa.String(50), unique=True, nullable=False),
        sa.Column('created_at', sa.DateTime(), default=sa.func.now()))


def downgrade():
    op.drop_table('users')
