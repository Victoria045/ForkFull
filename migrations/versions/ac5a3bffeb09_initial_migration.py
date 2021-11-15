"""Initial Migration

Revision ID: ac5a3bffeb09
Revises: 
Create Date: 2021-11-15 13:41:29.293204

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ac5a3bffeb09'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('uploads',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=255), nullable=False),
    sa.Column('category', sa.String(length=255), nullable=False),
    sa.Column('price', sa.Integer(), nullable=False),
    sa.Column('time_posted', sa.DateTime(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('upload', sa.Text(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_uploads_category'), 'uploads', ['category'], unique=False)
    op.create_index(op.f('ix_uploads_price'), 'uploads', ['price'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_uploads_price'), table_name='uploads')
    op.drop_index(op.f('ix_uploads_category'), table_name='uploads')
    op.drop_table('uploads')
    op.drop_table('users')
    # ### end Alembic commands ###