from sqlalchemy import Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship

from .base import BaseModel, Base

banner_image_association = Table(
    'banner_image_association',
    Base.metadata,
    Column('banner_id', Integer, ForeignKey('banners.id')),
    Column('banner_image_id', Integer, ForeignKey('images.id'))
)

product_type_image_association = Table(
    'product_type_image_association',
    Base.metadata,
    Column('product_type_id', Integer, ForeignKey('product_types.id')),
    Column('banner_image_id', Integer, ForeignKey('images.id'))
)

category_promotion_image_association = Table(
    'category_promotion_image_association',
    Base.metadata,
    Column('category_type_id', Integer, ForeignKey('category_types.id')),
    Column('banner_image_id', Integer, ForeignKey('images.id'))
)


class Image(BaseModel):
    __tablename__ = 'images'

    original = Column(String, nullable=False)
    thumbnail = Column(String, nullable=False)

    author_image = relationship('Author', back_populates='image')
    author_cover_image = relationship('Author', back_populates='cover_image')

    shops_logos = relationship('Shop', back_populates='logo')
    categories = relationship('Category', back_populates='image')
    shops_cover_image = relationship('Shop', back_populates='cover_image')
    banners = relationship('Banner', secondary=banner_image_association, back_populates='images')
    product_types = relationship(
        'ProductType',
        secondary=product_type_image_association,
        back_populates='promotional_sliders',
    )
    promotional_sliders = relationship(
        'CategoryType',
        secondary=category_promotion_image_association,
        back_populates='promotional_sliders',
    )
