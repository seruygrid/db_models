from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship

from .base import BaseModel


class Rating(BaseModel):
    __tablename__ = 'ratings'

    rating = Column(Integer, nullable=False)
    total = Column(Integer, nullable=False)
    positive_feedbacks_count = Column(Integer, nullable=False)
    negative_feedbacks_count = Column(Integer, nullable=False)
    my_feedback = Column(String)
    abusive_reports_count = Column(Integer, nullable=False)

    product_id = Column(Integer, ForeignKey('products.id'))

    product = relationship('Product', back_populates='rating_count')
