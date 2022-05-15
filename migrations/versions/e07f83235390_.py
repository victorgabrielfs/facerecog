"""empty message

Revision ID: e07f83235390
Revises: e8ac3ba0f1d0
Create Date: 2022-05-14 23:19:09.527294

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e07f83235390'
down_revision = 'e8ac3ba0f1d0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('images_picture_key', 'images', type_='unique')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint('images_picture_key', 'images', ['picture'])
    # ### end Alembic commands ###
