from sqlalchemy import Column, Integer, String, JSON, ForeignKey, Table, TIMESTAMP
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
    details = Column(String)
    language = Column(String(2), nullable=False)
    translated_languages = Column(JSON)
    deleted_at = Column(TIMESTAMP(timezone=True), nullable=True)

    parent_id = Column(Integer, ForeignKey('categories.id'))
    image_id = Column(Integer, ForeignKey('images.id'))

    image = relationship('Image', back_populates='child_category')
    parent = relationship('Category', remote_side='Category.id')
    products = relationship('Product', secondary=product_child_category_association, back_populates='child_categories')
