import factory

from .image import ImageFactory
from .base import BaseFactory
from ..db_models import OwnerProfile


class OwnerProfileFactory(BaseFactory):
    class Meta:
        model = OwnerProfile
        sqlalchemy_session_persistence = 'commit'

    bio = factory.Faker('paragraph')
    contact = factory.Faker('word')
    customer_id = factory.Faker('pyint')
    socials = [
        {
            'url': 'https://example.com',
            'icon': 'https://logo.com'
        } for _ in range(3)
    ]

    avatar = factory.SubFactory(ImageFactory)
