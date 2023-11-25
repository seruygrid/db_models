from enum import Enum

from sqlalchemy import Enum as SaEnum

from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship

from .base import BaseModel


class CustomerAddressType(str, Enum):
    BILLING: str = 'billing'
    SHIPPING: str = 'shipping'


class CustomerAddress(BaseModel):
    __tablename__ = 'customer_addresses'

    title = Column(String)
    type = Column(SaEnum(CustomerAddressType))
    default = Column(Integer)

    customer_id = Column(Integer, ForeignKey('customers.id'))
    address_id = Column(Integer, ForeignKey('addresses.id'))

    customer = relationship('Customer', back_populates='customer_address')
    address = relationship('Address', back_populates='customer_address')
