import factory

from .base import BaseFactory
from ..db_models import ShippingClass


class ShippingFactory(BaseFactory):
    class Meta:
        model = ShippingClass
        sqlalchemy_session_persistence = 'commit'

    name = factory.Faker('word')
    amount = factory.Faker('pyfloat')
    is_global = factory.Faker('pybool')
    type = factory.Faker('word')
