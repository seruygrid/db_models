from sqlalchemy import Column, String, JSON
from sqlalchemy.orm import relationship

from .base import BaseModel


class CategoryType(BaseModel):
    __tablename__ = 'category_types'

    name = Column(String, nullable=False)
    language = Column(String(2), nullable=False)
    translated_languages = Column(JSON)
    settings = Column(JSON)

    promotional_sliders = relationship('Image', back_populates='product_types')
    categories = relationship('Category', back_populates='type')
