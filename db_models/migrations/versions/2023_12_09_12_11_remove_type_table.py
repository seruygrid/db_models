"""remove type table

Revision ID: cdb6a8795ba4
Revises: f2e2361c1472
Create Date: 2023-12-09 12:11:21.184202

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = 'cdb6a8795ba4'
down_revision: Union[str, None] = 'f2e2361c1472'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('banners_product_type_id_fkey', 'banners', type_='foreignkey')
    op.drop_column('banners', 'product_type_id')
    op.add_column('categories', sa.Column('image_id', sa.Integer(), nullable=True))
    op.drop_constraint('categories_type_id_fkey', 'categories', type_='foreignkey')
    op.create_foreign_key('category_image_fkey', 'categories', 'images', ['image_id'], ['id'])
    op.drop_column('categories', 'image')
    op.drop_column('categories', 'type_id')
    op.add_column('child_categories', sa.Column('image_id', sa.Integer(), nullable=True))
    op.drop_constraint('child_categories_type_id_fkey', 'child_categories', type_='foreignkey')
    op.create_foreign_key('child_category_image_fkey', 'child_categories', 'images', ['image_id'], ['id'])
    op.drop_column('child_categories', 'image')
    op.drop_column('child_categories', 'type_id')
    op.drop_constraint('products_type_id_fkey', 'products', type_='foreignkey')
    op.drop_column('products', 'type_id')
    op.drop_table('category_promotion_image_association')
    op.drop_table('types')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('products', sa.Column('type_id', sa.INTEGER(), autoincrement=False, nullable=True))
    op.create_foreign_key('products_type_id_fkey', 'products', 'types', ['type_id'], ['id'])
    op.add_column('child_categories', sa.Column('type_id', sa.INTEGER(), autoincrement=False, nullable=False))
    op.add_column('child_categories',
                  sa.Column('image', postgresql.ARRAY(sa.VARCHAR()), autoincrement=False, nullable=True))
    op.drop_constraint('child_category_image_fkey', 'child_categories', type_='foreignkey')
    op.create_foreign_key('child_categories_type_id_fkey', 'child_categories', 'types', ['type_id'], ['id'])
    op.drop_column('child_categories', 'image_id')
    op.add_column('categories', sa.Column('type_id', sa.INTEGER(), autoincrement=False, nullable=False))
    op.add_column('categories', sa.Column('image', postgresql.ARRAY(sa.VARCHAR()), autoincrement=False, nullable=True))
    op.drop_constraint('category_image_fkey', 'categories', type_='foreignkey')
    op.create_foreign_key('categories_type_id_fkey', 'categories', 'types', ['type_id'], ['id'])
    op.drop_column('categories', 'image_id')
    op.add_column('banners', sa.Column('product_type_id', sa.INTEGER(), autoincrement=False, nullable=True))
    op.create_foreign_key('banners_product_type_id_fkey', 'banners', 'types', ['product_type_id'], ['id'])
    op.create_table(
        'types',
        sa.Column('name', sa.VARCHAR(), autoincrement=False, nullable=False),
        sa.Column('slug', sa.VARCHAR(), autoincrement=False, nullable=False),
        sa.Column('language', sa.VARCHAR(length=2), autoincrement=False, nullable=False),
        sa.Column('icon', sa.VARCHAR(), autoincrement=False, nullable=True),
        sa.Column('settings', postgresql.JSON(astext_type=sa.Text()), autoincrement=False, nullable=True),
        sa.Column('translated_languages', postgresql.JSON(astext_type=sa.Text()), autoincrement=False,
                  nullable=True),
        sa.Column('id', sa.INTEGER(), server_default=sa.text("nextval('types_id_seq'::regclass)"),
                  autoincrement=True, nullable=False),
        sa.Column('created_at', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('now()'),
                  autoincrement=False, nullable=False),
        sa.Column('updated_at', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('now()'),
                  autoincrement=False, nullable=False),
        sa.PrimaryKeyConstraint('id', name='types_pkey'),
        sa.UniqueConstraint('slug', name='types_slug_key'),
        postgresql_ignore_search_path=False
    )
    op.create_table(
        'category_promotion_image_association',
        sa.Column('category_type_id', sa.INTEGER(), autoincrement=False, nullable=True),
        sa.Column('image_id', sa.INTEGER(), autoincrement=False, nullable=True),
        sa.ForeignKeyConstraint(['category_type_id'], ['types.id'],
                                name='category_promotion_image_association_category_type_id_fkey'),
        sa.ForeignKeyConstraint(['image_id'], ['images.id'],
                                name='category_promotion_image_association_image_id_fkey')
    )
    # ### end Alembic commands ###
