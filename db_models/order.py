from sqlalchemy import Column, String, Integer, DECIMAL, ForeignKey, Table
from sqlalchemy.orm import relationship

from .base import BaseModel, Base

order_products_association = Table(
    'order_products_association',
    Base.metadata,
    Column('product_id', Integer, ForeignKey('products.id')),
    Column('order_id', Integer, ForeignKey('orders.id'))
)


class Order(BaseModel):
    __tablename__ = 'orders'

    tracking_number = Column(String, nullable=False)
    customer_contact = Column(String)
    amount = Column(DECIMAL)
    sales_tax = Column(DECIMAL)
    paid_total = Column(DECIMAL)
    total = Column(DECIMAL)
    cancelled_amount = Column(DECIMAL)
    discount = Column(DECIMAL)
    delivery_fee = Column(DECIMAL)
    language = Column(String(2))
    payment_gateway = Column(String)
    logistics_provider = Column(String)
    delivery_time = Column(String)
    order_status = Column(String)
    payment_status = Column(String)

    shipping_address_id = Column(Integer, ForeignKey('addresses.id'))
    billing_address_id = Column(Integer, ForeignKey('addresses.id'))
    customer_id = Column(Integer, ForeignKey('customers.id'))

    shipping_address = relationship('Address', back_populates='orders_ship', foreign_keys=[shipping_address_id])
    billing_address = relationship('Address', back_populates='orders_bill', foreign_keys=[billing_address_id])
    customer = relationship('Customer', back_populates='orders')
    children = relationship('ChildOrder', back_populates='order')
    products = relationship(
        'Product',
        secondary=order_products_association,
        back_populates='orders',
    )
