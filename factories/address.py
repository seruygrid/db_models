import factory

from .base import BaseFactory
from ..db_models import Address


class AddressFactory(BaseFactory):
    class Meta:
        model = Address
        sqlalchemy_session_persistence = 'commit'

    zip = factory.Faker('postcode')
    city = factory.Faker('city')
    state = factory.Faker('state_abbr')
    country = factory.Faker('country')
    street_address = factory.Faker('street_address')
