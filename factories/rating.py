import factory

from .product import ProductFactory
from .base import BaseFactory
from ..db_models import Rating


class RatingFactory(BaseFactory):
    class Meta:
        model = Rating
        sqlalchemy_session_persistence = 'commit'

    rating = factory.Faker('pyint')
    total = factory.Faker('pyint')
    positive_feedbacks_count = factory.Faker('pyint')
    negative_feedbacks_count = factory.Faker('pyint')
    my_feedback = factory.Faker('paragraph')
    abusive_reports_count = factory.Faker('pyint')

    product = factory.SubFactory(ProductFactory)
