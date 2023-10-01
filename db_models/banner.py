from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from .base import BaseModel


class Banner(BaseModel):
    __tablename__ = 'banners'

    type_id = Column(Integer, nullable=False)
    title = Column(String, nullable=False)
    description = Column(String, nullable=False)

    product_type_id = Column(Integer, ForeignKey('product_types.id'))
    image_id = Column(Integer, ForeignKey('images.id'))

    product_type = relationship('ProductType', back_populates='banners')
    image = relationship('Image', back_populates='banners')
