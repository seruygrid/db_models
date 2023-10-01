from sqlalchemy import Column, String, Boolean, DateTime, Integer, JSON, ForeignKey
from sqlalchemy.orm import relationship

from .base import BaseModel


class Author(BaseModel):
    __tablename__ = 'authors'

    name = Column(String, nullable=False)
    is_approved = Column(Boolean, nullable=False)
    slug = Column(String, unique=True, nullable=False)
    language = Column(String(2), nullable=False)
    bio = Column(String, nullable=False)
    quote = Column(String)
    born = Column(DateTime)
    languages = Column(String)
    products_count = Column(Integer)
    translated_languages = Column(JSON)

    image_id = Column(Integer, ForeignKey('images.id'))
    cover_image_id = Column(Integer, ForeignKey('images.id'))

    image = relationship('Image', back_populates='author_image', foreign_keys=[image_id])
    cover_image = relationship('Image', back_populates='author_cover_image', foreign_keys=[cover_image_id])
    products = relationship('Product', back_populates='author')
    shops = relationship('Shop', back_populates='owner')
