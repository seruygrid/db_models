from sqlalchemy import Column, Integer, String, ForeignKey, Boolean
from sqlalchemy.orm import relationship

from .base import BaseModel


class Shop(BaseModel):
    __tablename__ = 'shops'

    name = Column(String, nullable=False)
    description = Column(String, nullable=False)
    slug = Column(String, unique=True, nullable=False)
    is_active = Column(Boolean, default=True, nullable=False)

    logo_id = Column(Integer, ForeignKey('images.id'))
    address_id = Column(Integer, ForeignKey('addresses.id'))
    cover_image_id = Column(Integer, ForeignKey('images.id'))
    settings_id = Column(Integer, ForeignKey('shop_settings.id'))
    owner_id = Column(Integer, ForeignKey('customers.id'), nullable=False)

    owner = relationship('Customer', back_populates='shops')
    products = relationship('Product', back_populates='shop')
    settings = relationship('ShopSetting', back_populates='shop')
    child_orders = relationship('ChildOrder', back_populates='shop')
    logo = relationship('Image', back_populates='shops_logos', foreign_keys=[logo_id])
    address = relationship('Address', back_populates='shops', foreign_keys=[address_id])
    cover_image = relationship('Image', back_populates='shops_cover_image', foreign_keys=[cover_image_id])
