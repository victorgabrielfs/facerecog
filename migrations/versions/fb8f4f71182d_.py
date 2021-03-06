"""empty message

Revision ID: fb8f4f71182d
Revises: a480a91405cd
Create Date: 2022-05-14 22:56:45.670632

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fb8f4f71182d'
down_revision = 'a480a91405cd'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('images', 'mimetype')
    op.drop_column('images', 'filename')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('images', sa.Column('filename', sa.VARCHAR(length=25), autoincrement=False, nullable=False))
    op.add_column('images', sa.Column('mimetype', sa.VARCHAR(length=15), autoincrement=False, nullable=False))
    # ### end Alembic commands ###
