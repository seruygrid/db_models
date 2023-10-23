import factory

from .base import BaseFactory
from ..db_models import Location


class LocationFactory(BaseFactory):
    class Meta:
        model = Location
        sqlalchemy_session_persistence = 'commit'

    lat = factory.Faker('pystr')
    lng = factory.Faker('pystr')
    city = factory.Faker('city')
    state = factory.Faker('state')
    country = factory.Faker('country')
    formattedAddress = factory.Faker('address')
