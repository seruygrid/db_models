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

    shops = relationship('Shop', back_populates='address')
    orders_ship = relationship('Order', back_populates='shipping_address', foreign_keys='[Order.shipping_address_id]')
    orders_bill = relationship('Order', back_populates='billing_address', foreign_keys='[Order.billing_address_id]')
    customer_address = relationship('CustomerAddress', back_populates='address')
