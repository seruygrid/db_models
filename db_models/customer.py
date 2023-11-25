from sqlalchemy import Column, Integer, String, ForeignKey, Boolean, TIMESTAMP, Table
from sqlalchemy.orm import relationship

from .base import BaseModel, Base

customer_permission_association = Table(
    'customer_permission_association',
    Base.metadata,
    Column('customer_id', Integer, ForeignKey('customers.id')),
    Column('permission_id', Integer, ForeignKey('permissions.id'))
)


class Customer(BaseModel):
    __tablename__ = 'customers'

    sub = Column(String, nullable=False)
    name = Column(String, nullable=False)
    is_active = Column(Boolean, default=False)
    email = Column(String, unique=True, nullable=False)
    email_verified_at = Column(TIMESTAMP(timezone=True), nullable=True)

    shop_id = Column(Integer, ForeignKey('shops.id'))
    profile_id = Column(Integer, ForeignKey('profiles.id'))
    address_id = Column(Integer, ForeignKey('customer_addresses.id'))

    shop = relationship('Shop', back_populates='customer')
    orders = relationship('Order', back_populates='customer')
    profile = relationship('Profile', back_populates='customer')
    address = relationship('CustomerAddress', back_populates='customer')
    permissions = relationship('Permission', secondary=customer_permission_association, back_populates='customers')
