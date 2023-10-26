from sqlalchemy import Column, String, Integer, TIMESTAMP
from sqlalchemy.orm import relationship

from .base import BaseModel


class Customer(BaseModel):
    __tablename__ = 'customers'

    name = Column(String, nullable=False)
    email = Column(String)
    email_verified_at = Column(TIMESTAMP(timezone=True), nullable=True)
    is_active = Column(Integer)

    orders = relationship('Order', back_populates='customer')
