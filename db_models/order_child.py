from sqlalchemy import Column, String, Integer, DECIMAL, ForeignKey, Table
from sqlalchemy.orm import relationship

from .base import BaseModel, Base

child_order_products_association = Table(
    'child_order_products_association',
    Base.metadata,
    Column('product_id', Integer, ForeignKey('products.id')),
    Column('child_order_id', Integer, ForeignKey('child_orders.id'))
)


class ChildOrder(BaseModel):
    __tablename__ = 'child_orders'

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

    shop_id = Column(Integer, ForeignKey('shops.id'))
    parent_id = Column(Integer, ForeignKey('orders.id'))

    products = relationship(
        'Product',
        secondary=child_order_products_association,
        back_populates='child_orders',
    )
    order = relationship('Order', back_populates='children')
    shop = relationship('Shop', back_populates='child_orders')
