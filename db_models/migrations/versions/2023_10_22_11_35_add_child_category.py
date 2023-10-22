"""add child category

Revision ID: d4ed36dfee2e
Revises: 24316106db73
Create Date: 2023-10-22 11:35:22.047963

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = 'd4ed36dfee2e'
down_revision: Union[str, None] = '24316106db73'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        'child_categories',
        sa.Column('name', sa.String(), nullable=False),
        sa.Column('slug', sa.String(), nullable=False),
        sa.Column('icon', sa.String(), nullable=True),
        sa.Column('image', sa.ARRAY(sa.String()), nullable=True),
        sa.Column('details', sa.String(), nullable=True),
        sa.Column('language', sa.String(length=2), nullable=False),
        sa.Column('translated_languages', sa.JSON(), nullable=True),
        sa.Column('deleted_at', sa.TIMESTAMP(timezone=True), nullable=True),
        sa.Column('parent_id', sa.Integer(), nullable=True),
        sa.Column('type_id', sa.Integer(), nullable=False),
        sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
        sa.Column('created_at', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('now()'),
                  nullable=False),
        sa.Column('updated_at', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('now()'),
                  nullable=False),
        sa.ForeignKeyConstraint(['parent_id'], ['categories.id'], ),
        sa.ForeignKeyConstraint(['type_id'], ['category_types.id'], ),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('slug')
    )
    op.create_table(
        'product_child_category_association',
        sa.Column('product_id', sa.Integer(), nullable=True),
        sa.Column('child_category_id', sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(['child_category_id'], ['child_categories.id'], ),
        sa.ForeignKeyConstraint(['product_id'], ['products.id'], )
    )
    op.add_column('categories', sa.Column('image', sa.ARRAY(sa.String()), nullable=True))
    op.add_column('categories', sa.Column('deleted_at', sa.TIMESTAMP(timezone=True), nullable=True))
    op.drop_constraint('categories_parent_id_fkey', 'categories', type_='foreignkey')
    op.drop_column('categories', 'parent_id')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('categories', sa.Column('parent_id', sa.INTEGER(), autoincrement=False, nullable=True))
    op.create_foreign_key('categories_parent_id_fkey', 'categories', 'categories', ['parent_id'], ['id'])
    op.drop_column('categories', 'deleted_at')
    op.drop_column('categories', 'image')
    op.drop_table('product_child_category_association')
    op.drop_table('child_categories')
    # ### end Alembic commands ###
