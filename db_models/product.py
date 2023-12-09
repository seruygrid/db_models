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
from .category import product_category_association
from .child_category import product_child_category_association
from .image import product_gallery_image_association
from .order import order_products_association
from .order_child import child_order_products_association


class Product(BaseModel):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    slug = Column(String, unique=True, nullable=False)
    description = Column(String, nullable=False)
    language = Column(String(2), nullable=False)
    price = Column(Float, nullable=False)
    sale_price = Column(Float, nullable=True)
    min_price = Column(Float, nullable=True)
    max_price = Column(Float, nullable=True)
    status = Column(String, nullable=False)
    unit = Column(String, nullable=False)
    deleted_at = Column(DateTime)
    is_digital = Column(Boolean, default=False)
    is_external = Column(Boolean, default=False)
    ratings = Column(Float)
    total_reviews = Column(Integer)
    in_wishlist = Column(Boolean, default=False)
    blocked_dates = Column(JSON)
    translated_languages = Column(JSON)
    my_review = Column(String)

    image_id = Column(Integer, ForeignKey('images.id'))
    shop_id = Column(Integer, ForeignKey('shops.id'))
    shipping_class_id = Column(Integer, ForeignKey('shipping_classes.id'))

    image = relationship('Image', back_populates='products')
    gallery = relationship('Image', back_populates='product_gallery', secondary=product_gallery_image_association)
    shop = relationship('Shop', back_populates='products')
    shipping_class = relationship('ShippingClass', back_populates='products')
    rating_count = relationship('Rating', back_populates='product')
    categories = relationship(
        'Category',
        secondary=product_category_association,
        back_populates='products',
    )
    child_categories = relationship(
        'ChildCategory',
        secondary=product_child_category_association,
        back_populates='products',
    )
    orders = relationship(
        'Order',
        secondary=order_products_association,
        back_populates='products',
    )
    child_orders = relationship(
        'ChildOrder',
        secondary=child_order_products_association,
        back_populates='products',
    )
