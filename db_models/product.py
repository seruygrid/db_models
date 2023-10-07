from sqlalchemy import (
    Column,
    Integer,
    String,
    Float,
    Boolean,
    DateTime,
    ForeignKey,
    JSON,
)
from sqlalchemy.orm import relationship

from .base import BaseModel


class Product(BaseModel):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    slug = Column(String, unique=True, nullable=False)
    description = Column(String, nullable=False)
    price = Column(Float, nullable=False)
    sale_price = Column(Float)
    language = Column(String(2), nullable=False)
    min_price = Column(Float, nullable=False)
    max_price = Column(Float, nullable=False)
    sku = Column(String, unique=True)
    quantity = Column(Integer, nullable=False)
    in_stock = Column(Boolean, default=True)
    is_taxable = Column(Boolean, default=True)
    status = Column(String, nullable=False)
    product_type = Column(String, nullable=False)
    unit = Column(String, nullable=False)
    height = Column(Float)
    width = Column(Float)
    length = Column(Float)
    deleted_at = Column(DateTime)
    manufacturer_id = Column(Integer)
    is_digital = Column(Boolean, default=False)
    is_external = Column(Boolean, default=False)
    external_product_url = Column(String)
    external_product_button_text = Column(String)
    ratings = Column(Float)
    total_reviews = Column(Integer)
    in_wishlist = Column(Boolean, default=False)
    blocked_dates = Column(JSON)
    translated_languages = Column(JSON)
    my_review = Column(String)

    image_id = Column(Integer, ForeignKey('images.id'))
    author_id = Column(Integer, ForeignKey('authors.id'))
    type_id = Column(Integer, ForeignKey('product_types.id'))
    shop_id = Column(Integer, ForeignKey('shops.id'))
    shipping_class_id = Column(Integer, ForeignKey('shipping_classes.id'))

    image = relationship('Image', back_populates='products')
    author = relationship('Author', back_populates='products')
    type = relationship('ProductType', back_populates='products')
    shop = relationship('Shop', back_populates='products')
    shipping_class = relationship('ShippingClass', back_populates='products')
    rating_count = relationship('Rating', back_populates='product')
    categories = relationship(
        'Category',
        secondary='product_category_association',
        back_populates='products',
    )
