from sqlalchemy import Column, String, JSON
from sqlalchemy.orm import relationship

from .base import BaseModel
from .customer import customer_permission_association


class Permission(BaseModel):
    __tablename__ = 'permissions'

    name = Column(String, nullable=False, unique=True)
    guard_name = Column(String, nullable=False)
    pivot = Column(JSON, default=False)

    customers = relationship('Customer', secondary=customer_permission_association, back_populates='permissions')