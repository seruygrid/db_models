from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

from .base import BaseModel


class Location(BaseModel):
    __tablename__ = 'locations'

    lat = Column(String, nullable=False)
    lng = Column(String, nullable=False)
    city = Column(String, nullable=False)
    state = Column(String, nullable=True)
    country = Column(String, nullable=False)
    formattedAddress = Column(String, nullable=False)

    shop_settings = relationship('ShopSetting', back_populates='location')
