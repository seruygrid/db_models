from sqlalchemy import Column, Integer, String, ForeignKey, Boolean
from sqlalchemy.orm import relationship

from .base import BaseModel


class Shop(BaseModel):
    __tablename__ = 'shops'

    name = Column(String, nullable=False)
    slug = Column(String, unique=True, nullable=False)
    description = Column(String, nullable=False)
    is_active = Column(Boolean, default=True, nullable=False)

    logo_id = Column(Integer, ForeignKey('images.id'))
    cover_image_id = Column(Integer, ForeignKey('images.id'))
    owner_id = Column(Integer, ForeignKey('authors.id'), nullable=False)

    logo = relationship('Image', back_populates='shops_logos')
    owner = relationship('Author', back_populates='shops')
    cover_image = relationship('Image', back_populates='shops_cover_image')
    products = relationship('Product', back_populates='shop')
