from sqlalchemy import Column, String, Integer, ForeignKey, JSON
from sqlalchemy.orm import relationship

from .base import BaseModel


class OwnerProfile(BaseModel):
    __tablename__ = 'owner_profiles'

    bio = Column(String)
    socials = Column(JSON, nullable=True)
    contact = Column(String)

    customer_id = Column(Integer)

    avatar_id = Column(Integer, ForeignKey('images.id'))

    avatar = relationship('Image', back_populates='profiles')
    shop_owner = relationship('ShopOwner', back_populates='profile')
