from sqlalchemy import Column, Integer, String, JSON, ForeignKey, Table
from sqlalchemy.orm import relationship

from .base import BaseModel, Base

product_type_image_association = Table(
    'product_category_association',
    Base.metadata,
    Column('product_id', Integer, ForeignKey('products.id')),
    Column('category_id', Integer, ForeignKey('categories.id'))
)


class Category(BaseModel):
    __tablename__ = 'categories'

    name = Column(String, nullable=False)
    slug = Column(String, unique=True, nullable=False)
    icon = Column(String)
    details = Column(String)
    language = Column(String(2), nullable=False)
    translated_languages = Column(JSON)

    parent_id = Column(Integer, ForeignKey('categories.id'))
    type_id = Column(Integer, ForeignKey('category_types.id'), nullable=False)

    parent = relationship('Category', remote_side='Category.id')
    children = relationship('Category', back_populates='parent', remote_side='Category.parent_id')

    type = relationship('CategoryType', back_populates='categories')
    products = relationship('Product', secondary=product_type_image_association, back_populates='categories')
