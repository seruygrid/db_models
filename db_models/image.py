from sqlalchemy import Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship

from .base import BaseModel, Base

product_gallery_image_association = Table(
    'product_gallery_image_association',
    Base.metadata,
    Column('product_gallery_id', Integer, ForeignKey('products.id')),
    Column('image_id', Integer, ForeignKey('images.id'))
)


class Image(BaseModel):
    __tablename__ = 'images'

    original = Column(String, nullable=False)
    thumbnail = Column(String, nullable=False)

    author_image = relationship('Author', back_populates='image', foreign_keys='[Author.image_id]')
    author_cover_image = relationship('Author', back_populates='cover_image', foreign_keys='[Author.cover_image_id]')
    products = relationship('Product', back_populates='image')
    product_gallery = relationship('Product', back_populates='gallery', secondary=product_gallery_image_association)
    shops_logos = relationship('Shop', back_populates='logo', foreign_keys='[Shop.logo_id]')
    shops_cover_image = relationship('Shop', back_populates='cover_image', foreign_keys='[Shop.cover_image_id]')
    banners = relationship('Banner', back_populates='image')
    profiles = relationship('Profile', back_populates='avatar')
    category = relationship('Category', back_populates='image')
    child_category = relationship('ChildCategory', back_populates='image')
