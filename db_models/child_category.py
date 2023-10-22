from sqlalchemy import Column, Integer, String, JSON, ForeignKey, Table, ARRAY, TIMESTAMP
from sqlalchemy.orm import relationship

from .base import BaseModel, Base

product_child_category_association = Table(
    'product_child_category_association',
    Base.metadata,
    Column('product_id', Integer, ForeignKey('products.id')),
    Column('child_category_id', Integer, ForeignKey('child_categories.id'))
)


class ChildCategory(BaseModel):
    __tablename__ = 'child_categories'

    name = Column(String, nullable=False)
    slug = Column(String, unique=True, nullable=False)
    icon = Column(String)
    image = Column(ARRAY(String))
    details = Column(String)
    language = Column(String(2), nullable=False)
    translated_languages = Column(JSON)
    deleted_at = Column(TIMESTAMP(timezone=True), nullable=True)

    parent_id = Column(Integer, ForeignKey('categories.id'))
    type_id = Column(Integer, ForeignKey('category_types.id'), nullable=False)

    parent = relationship('Category', remote_side='Category.id')
    type = relationship('CategoryType', back_populates='child_categories')
    products = relationship('Product', secondary=product_child_category_association, back_populates='child_categories')
