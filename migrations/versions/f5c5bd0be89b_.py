"""empty message

Revision ID: f5c5bd0be89b
Revises: 
Create Date: 2023-05-05 12:02:31.909025

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f5c5bd0be89b'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('nick', sa.String(length=255), nullable=True))
        batch_op.create_unique_constraint(None, ['nick'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='unique')
        batch_op.drop_column('nick')

    # ### end Alembic commands ###