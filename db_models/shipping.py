from sqlalchemy import Column, String, Float, Boolean
from sqlalchemy.orm import relationship

from .base import BaseModel


class ShippingClass(BaseModel):
    __tablename__ = 'shipping_classes'

    name = Column(String, nullable=False)
    amount = Column(Float, nullable=False)
    is_global = Column(Boolean, nullable=False)
    type = Column(String, nullable=False)

    products = relationship('Product', back_populates='shipping_class')
