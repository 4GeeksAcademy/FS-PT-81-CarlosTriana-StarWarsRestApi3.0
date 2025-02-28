"""empty message

Revision ID: c86e6cac4b4f
Revises: 
Create Date: 2025-01-27 18:14:24.585005

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c86e6cac4b4f'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('favorites',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('people', sa.String(length=30), nullable=True),
    sa.Column('gender', sa.String(length=10), nullable=True),
    sa.Column('planet', sa.String(length=30), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('planets',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('planet', sa.String(length=80), nullable=False),
    sa.Column('rotation_period', sa.Float(), nullable=True),
    sa.Column('orbital_period', sa.Float(), nullable=True),
    sa.Column('gravity', sa.String(length=20), nullable=True),
    sa.Column('population', sa.Integer(), nullable=True),
    sa.Column('climate', sa.String(length=20), nullable=True),
    sa.Column('terrain', sa.String(length=20), nullable=True),
    sa.Column('surface_water', sa.Float(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('planet')
    )
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=120), nullable=False),
    sa.Column('password', sa.String(length=80), nullable=False),
    sa.Column('is_active', sa.Boolean(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('peoples',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('people', sa.String(length=80), nullable=False),
    sa.Column('gender', sa.String(length=20), nullable=True),
    sa.Column('birth_year', sa.Integer(), nullable=True),
    sa.Column('eye_color', sa.String(length=20), nullable=True),
    sa.Column('hair_color', sa.String(length=20), nullable=True),
    sa.Column('height', sa.Float(), nullable=True),
    sa.Column('mass', sa.Float(), nullable=True),
    sa.Column('skin_color', sa.String(length=20), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('people')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('peoples')
    op.drop_table('users')
    op.drop_table('planets')
    op.drop_table('favorites')
    # ### end Alembic commands ###
