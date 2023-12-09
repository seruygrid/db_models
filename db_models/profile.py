from sqlalchemy import Column, String, Integer, ForeignKey, JSON
from sqlalchemy.orm import relationship

from .base import BaseModel


class Profile(BaseModel):
    __tablename__ = 'profiles'

    bio = Column(String)
    socials = Column(JSON, nullable=True)
    contact = Column(String)

    avatar_id = Column(Integer, ForeignKey('images.id'))

    avatar = relationship('Image', back_populates='profiles')
    customer = relationship('Customer', back_populates='profile')
