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

    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    email_verified_at = Column(TIMESTAMP(timezone=True), nullable=True)
    is_active = Column(Boolean, default=False)

    shop_id = Column(Integer, ForeignKey('shops.id'))
    profile_id = Column(Integer, ForeignKey('profiles.id'))

    shop = relationship('Shop', back_populates='user')
    profile = relationship('Profile', back_populates='customer')
    address = relationship('Address', back_populates='shops')
    permissions = relationship('Permission', secondary=customer_permission_association, back_populates='customers')
