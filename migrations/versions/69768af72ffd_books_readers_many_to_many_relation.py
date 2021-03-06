"""Books_readers many to many relation

Revision ID: 69768af72ffd
Revises: 71d88f422166
Create Date: 2022-02-19 11:49:54.691714

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '69768af72ffd'
down_revision = '71d88f422166'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('books_readers',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('books_id', sa.Integer(), nullable=False),
    sa.Column('readers_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['books_id'], ['books.id'], ),
    sa.ForeignKeyConstraint(['readers_id'], ['readers.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('books_readers')
    # ### end Alembic commands ###
