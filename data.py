"""Added address table

Revision ID: b9a12bcde06c
Revises: 7ba36b366eb7
Create Date: 2022-06-11 12:48:06.253609

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b9a12bcde06c'
down_revision = '7ba36b366eb7'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('address',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('created_date', sa.DateTime(), nullable=True),
    sa.Column('shipping_address', sa.Text(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['account.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('address')
    # ### end Alembic commands ###