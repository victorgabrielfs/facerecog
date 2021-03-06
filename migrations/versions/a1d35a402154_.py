"""empty message

Revision ID: a1d35a402154
Revises: 3346bf9a69ee
Create Date: 2022-04-28 19:28:10.188545

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a1d35a402154'
down_revision = '3346bf9a69ee'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.Column('email', sa.String(length=50), nullable=False),
    sa.Column('password', sa.String(length=50), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('missing_people',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.Column('birthday', sa.DateTime(), nullable=False),
    sa.Column('birthplace', sa.String(length=50), nullable=False),
    sa.Column('place_of_disappearance', sa.String(length=100), nullable=True),
    sa.Column('disappearance_details', sa.Text(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('images',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('picture', sa.LargeBinary(), nullable=False),
    sa.Column('isUserProfile', sa.Boolean(), nullable=False),
    sa.Column('isMissingPersonProfile', sa.Boolean(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('missing_person_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['missing_person_id'], ['missing_people.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('picture')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('images')
    op.drop_table('missing_people')
    op.drop_table('users')
    # ### end Alembic commands ###
