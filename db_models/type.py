from sqlalchemy import Column, String, JSON
from sqlalchemy.orm import relationship

from .image import type_promotion_image_association
from .base import BaseModel


class Type(BaseModel):
    __tablename__ = 'types'

    name = Column(String, nullable=False)
    slug = Column(String, unique=True, nullable=False)
    language = Column(String(2), nullable=False)
    icon = Column(String)
    settings = Column(JSON)
    translated_languages = Column(JSON)

    promotional_sliders = relationship(
        'Image',
        secondary=type_promotion_image_association,
        back_populates='types',
    )
    categories = relationship('Category', back_populates='type')
    child_categories = relationship('ChildCategory', back_populates='type')
    banners = relationship('Banner', back_populates='product_type')
    products = relationship('Product', back_populates='type')
