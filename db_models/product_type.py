from sqlalchemy import Column, String, JSON
from sqlalchemy.orm import relationship

from .image import product_type_image_association
from .base import BaseModel


class ProductType(BaseModel):
    __tablename__ = 'product_types'

    name = Column(String, nullable=False)
    slug = Column(String, unique=True, nullable=False)
    language = Column(String(2), nullable=False)
    icon = Column(String)
    settings = Column(JSON, nullable=False)
    translated_languages = Column(JSON)

    banners = relationship('Banner', back_populates='product_type')
    promotional_sliders = relationship(
        'Image',
        secondary=product_type_image_association,
        back_populates='product_types',
    )
    products = relationship('Product', back_populates='type')
