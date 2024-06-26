"""empty message

Revision ID: a479381db76c
Revises: 
Create Date: 2024-06-21 10:16:12.272169

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'a479381db76c'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('customers',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('customername', sa.String(length=50), nullable=True),
    sa.Column('customeremail', sa.String(length=50), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('customer')
    op.drop_table('products')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('products',
    sa.Column('id', mysql.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('productname', mysql.VARCHAR(length=50), nullable=True),
    sa.Column('productUnit', mysql.VARCHAR(length=50), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.create_table('customer',
    sa.Column('id', mysql.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('customername', mysql.VARCHAR(length=150), nullable=True),
    sa.Column('customeremail', mysql.VARCHAR(length=150), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.drop_table('customers')
    # ### end Alembic commands ###
