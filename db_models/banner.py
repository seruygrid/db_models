from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from .base import BaseModel


class Banner(BaseModel):
    __tablename__ = 'banners'

    type_id = Column(Integer, nullable=False)
    title = Column(String, nullable=False)
    description = Column(String, nullable=False)

    image_id = Column(Integer, ForeignKey('images.id'))

    image = relationship('Image', back_populates='banners')
