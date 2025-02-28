"""empty message

Revision ID: 5acbdd5b5b83
Revises: c86e6cac4b4f
Create Date: 2025-01-27 18:42:56.952521

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5acbdd5b5b83'
down_revision = 'c86e6cac4b4f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('favorites', schema=None) as batch_op:
        batch_op.add_column(sa.Column('person', sa.String(length=30), nullable=True))
        batch_op.drop_column('people')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('favorites', schema=None) as batch_op:
        batch_op.add_column(sa.Column('people', sa.VARCHAR(length=30), autoincrement=False, nullable=True))
        batch_op.drop_column('person')

    # ### end Alembic commands ###
