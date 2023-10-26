"""init tables

Revision ID: 1acd5f6d0de4
Revises: 
Create Date: 2023-10-26 16:25:37.766436

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = '1acd5f6d0de4'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        'addresses',
        sa.Column('zip', sa.String(), nullable=False),
        sa.Column('city', sa.String(), nullable=False),
        sa.Column('state', sa.String(), nullable=False),
        sa.Column('country', sa.String(), nullable=False),
        sa.Column('street_address', sa.String(), nullable=False),
        sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
        sa.Column('created_at', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('now()'), nullable=False),
        sa.Column('updated_at', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('now()'), nullable=False),
        sa.PrimaryKeyConstraint('id')
    )
    op.create_table(
        'customers',
        sa.Column('name', sa.String(), nullable=False),
        sa.Column('email', sa.String(), nullable=True),
        sa.Column('email_verified_at', sa.TIMESTAMP(timezone=True), nullable=True),
        sa.Column('is_active', sa.Integer(), nullable=True),
        sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
        sa.Column('created_at', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('now()'),
                  nullable=False),
        sa.Column('updated_at', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('now()'),
                  nullable=False),
        sa.PrimaryKeyConstraint('id')
    )
    op.create_table(
        'images',
        sa.Column('original', sa.String(), nullable=False),
        sa.Column('thumbnail', sa.String(), nullable=False),
        sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
        sa.Column('created_at', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('now()'),
                  nullable=False),
        sa.Column('updated_at', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('now()'),
                  nullable=False),
        sa.PrimaryKeyConstraint('id')
    )
    op.create_table(
        'locations',
        sa.Column('lat', sa.String(), nullable=False),
        sa.Column('lng', sa.String(), nullable=False),
        sa.Column('city', sa.String(), nullable=False),
        sa.Column('state', sa.String(), nullable=True),
        sa.Column('country', sa.String(), nullable=False),
        sa.Column('formattedAddress', sa.String(), nullable=False),
        sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
        sa.Column('created_at', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('now()'),
                  nullable=False),
        sa.Column('updated_at', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('now()'),
                  nullable=False),
        sa.PrimaryKeyConstraint('id')
    )
    op.create_table(
        'shipping_classes',
        sa.Column('name', sa.String(), nullable=False),
        sa.Column('amount', sa.Float(), nullable=False),
        sa.Column('is_global', sa.Boolean(), nullable=False),
        sa.Column('type', sa.String(), nullable=False),
        sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
        sa.Column('created_at', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('now()'),
                  nullable=False),
        sa.Column('updated_at', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('now()'),
                  nullable=False),
        sa.PrimaryKeyConstraint('id')
    )
    op.create_table(
        'types',
        sa.Column('name', sa.String(), nullable=False),
        sa.Column('slug', sa.String(), nullable=False),
        sa.Column('language', sa.String(length=2), nullable=False),
        sa.Column('icon', sa.String(), nullable=True),
        sa.Column('settings', sa.JSON(), nullable=True),
        sa.Column('translated_languages', sa.JSON(), nullable=True),
        sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
        sa.Column('created_at', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('now()'),
                  nullable=False),
        sa.Column('updated_at', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('now()'),
                  nullable=False),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('slug')
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
        sa.Column('created_at', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('now()'),
                  nullable=False),
        sa.Column('updated_at', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('now()'),
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
        sa.Column('image_id', sa.Integer(), nullable=True),
        sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
        sa.Column('created_at', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('now()'),
                  nullable=False),
        sa.Column('updated_at', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('now()'),
                  nullable=False),
        sa.ForeignKeyConstraint(['image_id'], ['images.id'], ),
        sa.ForeignKeyConstraint(['product_type_id'], ['types.id'], ),
        sa.PrimaryKeyConstraint('id')
    )
    op.create_table(
        'categories',
        sa.Column('name', sa.String(), nullable=False),
        sa.Column('slug', sa.String(), nullable=False),
        sa.Column('icon', sa.String(), nullable=True),
        sa.Column('image', sa.ARRAY(sa.String()), nullable=True),
        sa.Column('details', sa.String(), nullable=True),
        sa.Column('language', sa.String(length=2), nullable=False),
        sa.Column('translated_languages', sa.JSON(), nullable=True),
        sa.Column('deleted_at', sa.TIMESTAMP(timezone=True), nullable=True),
        sa.Column('type_id', sa.Integer(), nullable=False),
        sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
        sa.Column('created_at', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('now()'),
                  nullable=False),
        sa.Column('updated_at', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('now()'),
                  nullable=False),
        sa.ForeignKeyConstraint(['type_id'], ['types.id'], ),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('slug')
    )
    op.create_table(
        'category_promotion_image_association',
        sa.Column('category_type_id', sa.Integer(), nullable=True),
        sa.Column('image_id', sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(['category_type_id'], ['types.id'], ),
        sa.ForeignKeyConstraint(['image_id'], ['images.id'], )
    )
    op.create_table(
        'orders',
        sa.Column('tracking_number', sa.String(), nullable=False),
        sa.Column('customer_contact', sa.String(), nullable=True),
        sa.Column('amount', sa.DECIMAL(), nullable=True),
        sa.Column('sales_tax', sa.DECIMAL(), nullable=True),
        sa.Column('paid_total', sa.DECIMAL(), nullable=True),
        sa.Column('total', sa.DECIMAL(), nullable=True),
        sa.Column('cancelled_amount', sa.DECIMAL(), nullable=True),
        sa.Column('discount', sa.DECIMAL(), nullable=True),
        sa.Column('delivery_fee', sa.DECIMAL(), nullable=True),
        sa.Column('language', sa.String(length=2), nullable=True),
        sa.Column('payment_gateway', sa.String(), nullable=True),
        sa.Column('logistics_provider', sa.String(), nullable=True),
        sa.Column('delivery_time', sa.String(), nullable=True),
        sa.Column('order_status', sa.String(), nullable=True),
        sa.Column('payment_status', sa.String(), nullable=True),
        sa.Column('shipping_address_id', sa.Integer(), nullable=True),
        sa.Column('billing_address_id', sa.Integer(), nullable=True),
        sa.Column('customer_id', sa.Integer(), nullable=True),
        sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
        sa.Column('created_at', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('now()'),
                  nullable=False),
        sa.Column('updated_at', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('now()'),
                  nullable=False),
        sa.ForeignKeyConstraint(['billing_address_id'], ['addresses.id'], ),
        sa.ForeignKeyConstraint(['customer_id'], ['customers.id'], ),
        sa.ForeignKeyConstraint(['shipping_address_id'], ['addresses.id'], ),
        sa.PrimaryKeyConstraint('id')
    )
    op.create_table(
        'owner_profiles',
        sa.Column('bio', sa.String(), nullable=True),
        sa.Column('socials', sa.JSON(), nullable=True),
        sa.Column('contact', sa.String(), nullable=True),
        sa.Column('customer_id', sa.Integer(), nullable=True),
        sa.Column('avatar_id', sa.Integer(), nullable=True),
        sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
        sa.Column('created_at', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('now()'),
                  nullable=False),
        sa.Column('updated_at', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('now()'),
                  nullable=False),
        sa.ForeignKeyConstraint(['avatar_id'], ['images.id'], ),
        sa.PrimaryKeyConstraint('id')
    )
    op.create_table(
        'shop_settings',
        sa.Column('contact', sa.String(), nullable=False),
        sa.Column('socials', sa.JSON(), nullable=False),
        sa.Column('website', sa.String(), nullable=False),
        sa.Column('location_id', sa.Integer(), nullable=True),
        sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
        sa.Column('created_at', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('now()'),
                  nullable=False),
        sa.Column('updated_at', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('now()'),
                  nullable=False),
        sa.ForeignKeyConstraint(['location_id'], ['locations.id'], ),
        sa.PrimaryKeyConstraint('id')
    )
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
        sa.ForeignKeyConstraint(['type_id'], ['types.id'], ),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('slug')
    )
    op.create_table(
        'shop_owners',
        sa.Column('name', sa.String(), nullable=False),
        sa.Column('email', sa.String(), nullable=True),
        sa.Column('email_verified_at', sa.TIMESTAMP(timezone=True), nullable=True),
        sa.Column('is_active', sa.Integer(), nullable=True),
        sa.Column('profile_id', sa.Integer(), nullable=True),
        sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
        sa.Column('created_at', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('now()'),
                  nullable=False),
        sa.Column('updated_at', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('now()'),
                  nullable=False),
        sa.ForeignKeyConstraint(['profile_id'], ['owner_profiles.id'], ),
        sa.PrimaryKeyConstraint('id')
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
        sa.Column('address_id', sa.Integer(), nullable=True),
        sa.Column('settings_id', sa.Integer(), nullable=True),
        sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
        sa.Column('created_at', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('now()'),
                  nullable=False),
        sa.Column('updated_at', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('now()'),
                  nullable=False),
        sa.ForeignKeyConstraint(['address_id'], ['addresses.id'], ),
        sa.ForeignKeyConstraint(['cover_image_id'], ['images.id'], ),
        sa.ForeignKeyConstraint(['logo_id'], ['images.id'], ),
        sa.ForeignKeyConstraint(['owner_id'], ['shop_owners.id'], ),
        sa.ForeignKeyConstraint(['settings_id'], ['shop_settings.id'], ),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('slug')
    )
    op.create_table(
        'child_orders',
        sa.Column('tracking_number', sa.String(), nullable=False),
        sa.Column('customer_contact', sa.String(), nullable=True),
        sa.Column('amount', sa.DECIMAL(), nullable=True),
        sa.Column('sales_tax', sa.DECIMAL(), nullable=True),
        sa.Column('paid_total', sa.DECIMAL(), nullable=True),
        sa.Column('total', sa.DECIMAL(), nullable=True),
        sa.Column('cancelled_amount', sa.DECIMAL(), nullable=True),
        sa.Column('discount', sa.DECIMAL(), nullable=True),
        sa.Column('delivery_fee', sa.DECIMAL(), nullable=True),
        sa.Column('language', sa.String(length=2), nullable=True),
        sa.Column('payment_gateway', sa.String(), nullable=True),
        sa.Column('logistics_provider', sa.String(), nullable=True),
        sa.Column('delivery_time', sa.String(), nullable=True),
        sa.Column('order_status', sa.String(), nullable=True),
        sa.Column('payment_status', sa.String(), nullable=True),
        sa.Column('shop_id', sa.Integer(), nullable=True),
        sa.Column('parent_id', sa.Integer(), nullable=True),
        sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
        sa.Column('created_at', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('now()'),
                  nullable=False),
        sa.Column('updated_at', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('now()'),
                  nullable=False),
        sa.ForeignKeyConstraint(['parent_id'], ['orders.id'], ),
        sa.ForeignKeyConstraint(['shop_id'], ['shops.id'], ),
        sa.PrimaryKeyConstraint('id')
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
        sa.Column('image_id', sa.Integer(), nullable=True),
        sa.Column('author_id', sa.Integer(), nullable=True),
        sa.Column('type_id', sa.Integer(), nullable=True),
        sa.Column('shop_id', sa.Integer(), nullable=True),
        sa.Column('shipping_class_id', sa.Integer(), nullable=True),
        sa.Column('created_at', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('now()'),
                  nullable=False),
        sa.Column('updated_at', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('now()'),
                  nullable=False),
        sa.ForeignKeyConstraint(['author_id'], ['authors.id'], ),
        sa.ForeignKeyConstraint(['image_id'], ['images.id'], ),
        sa.ForeignKeyConstraint(['shipping_class_id'], ['shipping_classes.id'], ),
        sa.ForeignKeyConstraint(['shop_id'], ['shops.id'], ),
        sa.ForeignKeyConstraint(['type_id'], ['types.id'], ),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('sku'),
        sa.UniqueConstraint('slug')
    )
    op.create_table(
        'child_order_products_association',
        sa.Column('product_id', sa.Integer(), nullable=True),
        sa.Column('child_order_id', sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(['child_order_id'], ['child_orders.id'], ),
        sa.ForeignKeyConstraint(['product_id'], ['products.id'], )
    )
    op.create_table(
        'order_products_association',
        sa.Column('product_id', sa.Integer(), nullable=True),
        sa.Column('order_id', sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(['order_id'], ['orders.id'], ),
        sa.ForeignKeyConstraint(['product_id'], ['products.id'], )
    )
    op.create_table(
        'product_category_association',
        sa.Column('product_id', sa.Integer(), nullable=True),
        sa.Column('category_id', sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(['category_id'], ['categories.id'], ),
        sa.ForeignKeyConstraint(['product_id'], ['products.id'], )
    )
    op.create_table(
        'product_child_category_association',
        sa.Column('product_id', sa.Integer(), nullable=True),
        sa.Column('child_category_id', sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(['child_category_id'], ['child_categories.id'], ),
        sa.ForeignKeyConstraint(['product_id'], ['products.id'], )
    )
    op.create_table(
        'product_gallery_image_association',
        sa.Column('product_gallery_id', sa.Integer(), nullable=True),
        sa.Column('image_id', sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(['image_id'], ['images.id'], ),
        sa.ForeignKeyConstraint(['product_gallery_id'], ['products.id'], )
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
        sa.Column('created_at', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('now()'),
                  nullable=False),
        sa.Column('updated_at', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('now()'),
                  nullable=False),
        sa.ForeignKeyConstraint(['product_id'], ['products.id'], ),
        sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('ratings')
    op.drop_table('product_gallery_image_association')
    op.drop_table('product_child_category_association')
    op.drop_table('product_category_association')
    op.drop_table('order_products_association')
    op.drop_table('child_order_products_association')
    op.drop_table('products')
    op.drop_table('child_orders')
    op.drop_table('shops')
    op.drop_table('shop_owners')
    op.drop_table('child_categories')
    op.drop_table('shop_settings')
    op.drop_table('owner_profiles')
    op.drop_table('orders')
    op.drop_table('category_promotion_image_association')
    op.drop_table('categories')
    op.drop_table('banners')
    op.drop_table('authors')
    op.drop_table('types')
    op.drop_table('shipping_classes')
    op.drop_table('locations')
    op.drop_table('images')
    op.drop_table('customers')
    op.drop_table('addresses')
    # ### end Alembic commands ###
