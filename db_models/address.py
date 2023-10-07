from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

from .base import BaseModel


class Address(BaseModel):
    __tablename__ = 'addresses'

    zip = Column(String, nullable=False)
    city = Column(String, nullable=False)
    state = Column(String, nullable=False)
    country = Column(String, nullable=False)
    street_address = Column(String, nullable=False)

    shops = relationship('Product', back_populates='address')
