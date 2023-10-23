from sqlalchemy import Column, String, Integer, ForeignKey, TIMESTAMP
from sqlalchemy.orm import relationship

from .base import BaseModel


class ShopOwner(BaseModel):
    __tablename__ = 'shop_owners'

    name = Column(String, nullable=False)
    email = Column(String)
    email_verified_at = Column(TIMESTAMP(timezone=True), nullable=True)
    is_active = Column(Integer)

    profile_id = Column(Integer, ForeignKey('owner_profiles.id'))

    shops = relationship('Shop', back_populates='owner')
    products = relationship('Product', back_populates='author')
    profile = relationship('OwnerProfile', back_populates='shop_owner')
