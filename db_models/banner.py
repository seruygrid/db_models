from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from .base import BaseModel
from .image import banner_image_association


class Banner(BaseModel):
    __tablename__ = 'banners'

    type_id = Column(Integer, nullable=False)
    title = Column(String, nullable=False)
    description = Column(String, nullable=False)

    product_type_id = Column(Integer, ForeignKey('product_types.id'))

    product_type = relationship('ProductType', back_populates='banners')
    images = relationship('Image', secondary=banner_image_association, back_populates='banners')
