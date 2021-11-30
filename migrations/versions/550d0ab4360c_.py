"""empty message

Revision ID: 550d0ab4360c
Revises: a8ab6c1a5199
Create Date: 2021-11-24 20:05:48.182110

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '550d0ab4360c'
down_revision = 'a8ab6c1a5199'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('monster_nft_holder', sa.Column('block_number', sa.String(length=50), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('monster_nft_holder', 'block_number')
    # ### end Alembic commands ###