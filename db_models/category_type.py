from sqlalchemy import Column, String, JSON
from sqlalchemy.orm import relationship

from .image import category_promotion_image_association
from .base import BaseModel


class CategoryType(BaseModel):
    __tablename__ = 'category_types'

    name = Column(String, nullable=False)
    slug = Column(String, unique=True, nullable=False)
    icon = Column(String)
    language = Column(String(2), nullable=False)
    translated_languages = Column(JSON)
    settings = Column(JSON)

    promotional_sliders = relationship(
        'Image',
        secondary=category_promotion_image_association,
        back_populates='category_types',
    )
    categories = relationship('Category', back_populates='type')
    child_categories = relationship('ChildCategory', back_populates='type')
