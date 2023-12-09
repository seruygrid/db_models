from sqlalchemy import Column, Integer, String, JSON, ForeignKey, Table, TIMESTAMP
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
    details = Column(String)
    language = Column(String(2), nullable=False)
    translated_languages = Column(JSON)
    deleted_at = Column(TIMESTAMP(timezone=True), nullable=True)

    image_id = Column(Integer, ForeignKey('images.id'))

    image = relationship('Image', back_populates='category')
    children = relationship('ChildCategory', back_populates='parent')
    products = relationship('Product', secondary=product_category_association, back_populates='categories')
