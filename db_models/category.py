from sqlalchemy import Column, Integer, String, JSON, ForeignKey, Table, ARRAY, TIMESTAMP
from sqlalchemy.orm import relationship

from .base import BaseModel, Base

product_category_association = Table(
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
    image = Column(ARRAY(String))
    details = Column(String)
    language = Column(String(2), nullable=False)
    translated_languages = Column(JSON)
    deleted_at = Column(TIMESTAMP(timezone=True), nullable=True)

    type_id = Column(Integer, ForeignKey('types.id'), nullable=False)

    type = relationship('Type', back_populates='categories')
    children = relationship('ChildCategory', back_populates='parent')
    products = relationship('Product', secondary=product_category_association, back_populates='categories')
