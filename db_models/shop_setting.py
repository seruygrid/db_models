from sqlalchemy import Column, String, JSON, Integer, ForeignKey
from sqlalchemy.orm import relationship

from .base import BaseModel


class ShopSetting(BaseModel):
    __tablename__ = 'shop_settings'

    contact = Column(String, nullable=False)
    socials = Column(JSON, nullable=False)
    website = Column(String, nullable=False)

    location_id = Column(Integer, ForeignKey('locations.id'))

    shop = relationship('Shop', back_populates='settings')
    location = relationship('Location', back_populates='shop_settings')
