import factory

from .base import BaseFactory
from ..db_models import Image


class ImageFactory(BaseFactory):
    class Meta:
        model = Image
        sqlalchemy_session_persistence = 'commit'

    original = factory.Faker('uri')
    thumbnail = factory.Faker('uri')
