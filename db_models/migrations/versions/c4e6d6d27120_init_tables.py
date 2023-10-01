"""init tables

Revision ID: c4e6d6d27120
Revises: 
Create Date: 2023-10-01 10:12:56.913732

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = 'c4e6d6d27120'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        'category_types',
        sa.Column('name', sa.String(), nullable=False),
        sa.Column('language', sa.String(length=2), nullable=False),
        sa.Column('translated_languages', sa.JSON(), nullable=True),
        sa.Column('settings', sa.JSON(), nullable=True),
        sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
        sa.Column('created', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('now()'),
                  nullable=False),
        sa.Column('updated', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('now()'),
                  nullable=False),
        sa.PrimaryKeyConstraint('id')
    )
    op.create_table(
        'images',
        sa.Column('original', sa.String(), nullable=False),
        sa.Column('thumbnail', sa.String(), nullable=False),
        sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
        sa.Column('created', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('now()'),
                  nullable=False),
        sa.Column('updated', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('now()'),
                  nullable=False),
        sa.PrimaryKeyConstraint('id')
    )
    op.create_table(
        'product_types',
        sa.Column('name', sa.String(), nullable=False),
        sa.Column('slug', sa.String(), nullable=False),
        sa.Column('language', sa.String(length=2), nullable=False),
        sa.Column('icon', sa.String(), nullable=True),
        sa.Column('settings', sa.JSON(), nullable=False),
        sa.Column('translated_languages', sa.JSON(), nullable=True),
        sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
        sa.Column('created', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('now()'),
                  nullable=False),
        sa.Column('updated', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('now()'),
                  nullable=False),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('slug')
    )
    op.create_table(
        'shipping_classes',
        sa.Column('name', sa.String(), nullable=False),
        sa.Column('amount', sa.Float(), nullable=False),
        sa.Column('is_global', sa.Boolean(), nullable=False),
        sa.Column('type', sa.String(), nullable=False),
        sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
        sa.Column('created', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('now()'),
                  nullable=False),
        sa.Column('updated', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('now()'),
                  nullable=False),
        sa.PrimaryKeyConstraint('id')
    )
    op.create_table(
        'authors',
        sa.Column('name', sa.String(), nullable=False),
        sa.Column('is_approved', sa.Boolean(), nullable=False),
        sa.Column('slug', sa.String(), nullable=False),
        sa.Column('language', sa.String(length=2), nullable=False),
        sa.Column('bio', sa.String(), nullable=False),
        sa.Column('quote', sa.String(), nullable=True),
        sa.Column('born', sa.DateTime(), nullable=True),
        sa.Column('languages', sa.String(), nullable=True),
        sa.Column('products_count', sa.Integer(), nullable=True),
        sa.Column('translated_languages', sa.JSON(), nullable=True),
        sa.Column('image_id', sa.Integer(), nullable=True),
        sa.Column('cover_image_id', sa.Integer(), nullable=True),
        sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
        sa.Column('created', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('now()'),
                  nullable=False),
        sa.Column('updated', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('now()'),
                  nullable=False),
        sa.ForeignKeyConstraint(['cover_image_id'], ['images.id'], ),
        sa.ForeignKeyConstraint(['image_id'], ['images.id'], ),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('slug')
    )
    op.create_table(
        'banners',
        sa.Column('type_id', sa.Integer(), nullable=False),
        sa.Column('title', sa.String(), nullable=False),
        sa.Column('description', sa.String(), nullable=False),
        sa.Column('product_type_id', sa.Integer(), nullable=True),
        sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
        sa.Column('created', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('now()'),
                  nullable=False),
        sa.Column('updated', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('now()'),
                  nullable=False),
        sa.ForeignKeyConstraint(['product_type_id'], ['product_types.id'], ),
        sa.PrimaryKeyConstraint('id')
    )
    op.create_table(
        'categories',
        sa.Column('name', sa.String(), nullable=False),
        sa.Column('slug', sa.String(), nullable=False),
        sa.Column('icon', sa.String(), nullable=True),
        sa.Column('details', sa.String(), nullable=True),
        sa.Column('language', sa.String(length=2), nullable=False),
        sa.Column('translated_languages', sa.JSON(), nullable=True),
        sa.Column('parent_id', sa.Integer(), nullable=True),
        sa.Column('type_id', sa.Integer(), nullable=False),
        sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
        sa.Column('created', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('now()'),
                  nullable=False),
        sa.Column('updated', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('now()'),
                  nullable=False),
        sa.ForeignKeyConstraint(['parent_id'], ['categories.id'], ),
        sa.ForeignKeyConstraint(['type_id'], ['category_types.id'], ),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('slug')
    )
    op.create_table(
        'category_promotion_image_association',
        sa.Column('category_type_id', sa.Integer(), nullable=True),
        sa.Column('banner_image_id', sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(['banner_image_id'], ['images.id'], ),
        sa.ForeignKeyConstraint(['category_type_id'], ['category_types.id'], )
    )
    op.create_table(
        'product_type_image_association',
        sa.Column('product_type_id', sa.Integer(), nullable=True),
        sa.Column('banner_image_id', sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(['banner_image_id'], ['images.id'], ),
        sa.ForeignKeyConstraint(['product_type_id'], ['product_types.id'], )
    )
    op.create_table(
        'banner_image_association',
        sa.Column('banner_id', sa.Integer(), nullable=True),
        sa.Column('banner_image_id', sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(['banner_id'], ['banners.id'], ),
        sa.ForeignKeyConstraint(['banner_image_id'], ['images.id'], )
    )
    op.create_table(
        'shops',
        sa.Column('name', sa.String(), nullable=False),
        sa.Column('slug', sa.String(), nullable=False),
        sa.Column('description', sa.String(), nullable=False),
        sa.Column('is_active', sa.Boolean(), nullable=False),
        sa.Column('logo_id', sa.Integer(), nullable=True),
        sa.Column('cover_image_id', sa.Integer(), nullable=True),
        sa.Column('owner_id', sa.Integer(), nullable=False),
        sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
        sa.Column('created', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('now()'),
                  nullable=False),
        sa.Column('updated', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('now()'),
                  nullable=False),
        sa.ForeignKeyConstraint(['cover_image_id'], ['images.id'], ),
        sa.ForeignKeyConstraint(['logo_id'], ['images.id'], ),
        sa.ForeignKeyConstraint(['owner_id'], ['authors.id'], ),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('slug')
    )
    op.create_table(
        'products',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('name', sa.String(), nullable=False),
        sa.Column('slug', sa.String(), nullable=False),
        sa.Column('description', sa.String(), nullable=False),
        sa.Column('price', sa.Float(), nullable=False),
        sa.Column('sale_price', sa.Float(), nullable=True),
        sa.Column('language', sa.String(length=2), nullable=False),
        sa.Column('min_price', sa.Float(), nullable=False),
        sa.Column('max_price', sa.Float(), nullable=False),
        sa.Column('sku', sa.String(), nullable=True),
        sa.Column('quantity', sa.Integer(), nullable=False),
        sa.Column('in_stock', sa.Boolean(), nullable=True),
        sa.Column('is_taxable', sa.Boolean(), nullable=True),
        sa.Column('status', sa.String(), nullable=False),
        sa.Column('product_type', sa.String(), nullable=False),
        sa.Column('unit', sa.String(), nullable=False),
        sa.Column('height', sa.Float(), nullable=True),
        sa.Column('width', sa.Float(), nullable=True),
        sa.Column('length', sa.Float(), nullable=True),
        sa.Column('deleted_at', sa.DateTime(), nullable=True),
        sa.Column('manufacturer_id', sa.Integer(), nullable=True),
        sa.Column('is_digital', sa.Boolean(), nullable=True),
        sa.Column('is_external', sa.Boolean(), nullable=True),
        sa.Column('external_product_url', sa.String(), nullable=True),
        sa.Column('external_product_button_text', sa.String(), nullable=True),
        sa.Column('ratings', sa.Float(), nullable=True),
        sa.Column('total_reviews', sa.Integer(), nullable=True),
        sa.Column('in_wishlist', sa.Boolean(), nullable=True),
        sa.Column('blocked_dates', sa.JSON(), nullable=True),
        sa.Column('translated_languages', sa.JSON(), nullable=True),
        sa.Column('my_review', sa.String(), nullable=True),
        sa.Column('author_id', sa.Integer(), nullable=True),
        sa.Column('type_id', sa.Integer(), nullable=True),
        sa.Column('shop_id', sa.Integer(), nullable=True),
        sa.Column('shipping_class_id', sa.Integer(), nullable=True),
        sa.Column('created', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('now()'),
                  nullable=False),
        sa.Column('updated', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('now()'),
                  nullable=False),
        sa.ForeignKeyConstraint(['author_id'], ['authors.id'], ),
        sa.ForeignKeyConstraint(['shipping_class_id'], ['shipping_classes.id'], ),
        sa.ForeignKeyConstraint(['shop_id'], ['shops.id'], ),
        sa.ForeignKeyConstraint(['type_id'], ['product_types.id'], ),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('sku'),
        sa.UniqueConstraint('slug')
    )
    op.create_table(
        'product_category_association',
        sa.Column('product_id', sa.Integer(), nullable=True),
        sa.Column('category_id', sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(['category_id'], ['categories.id'], ),
        sa.ForeignKeyConstraint(['product_id'], ['products.id'], )
    )
    op.create_table(
        'ratings',
        sa.Column('rating', sa.Integer(), nullable=False),
        sa.Column('total', sa.Integer(), nullable=False),
        sa.Column('positive_feedbacks_count', sa.Integer(), nullable=False),
        sa.Column('negative_feedbacks_count', sa.Integer(), nullable=False),
        sa.Column('my_feedback', sa.String(), nullable=True),
        sa.Column('abusive_reports_count', sa.Integer(), nullable=False),
        sa.Column('product_id', sa.Integer(), nullable=True),
        sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
        sa.Column('created', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('now()'),
                  nullable=False),
        sa.Column('updated', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('now()'),
                  nullable=False),
        sa.ForeignKeyConstraint(['product_id'], ['products.id'], ),
        sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('ratings')
    op.drop_table('product_category_association')
    op.drop_table('products')
    op.drop_table('shops')
    op.drop_table('banner_image_association')
    op.drop_table('product_type_image_association')
    op.drop_table('category_promotion_image_association')
    op.drop_table('categories')
    op.drop_table('banners')
    op.drop_table('authors')
    op.drop_table('shipping_classes')
    op.drop_table('product_types')
    op.drop_table('images')
    op.drop_table('category_types')
    # ### end Alembic commands ###