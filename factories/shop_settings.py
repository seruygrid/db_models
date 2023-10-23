import factory

from .location import LocationFactory
from .base import BaseFactory
from ..db_models import ShopSetting


class ShopSettingFactory(BaseFactory):
    class Meta:
        model = ShopSetting
        sqlalchemy_session_persistence = 'commit'

    contact = factory.Faker('phone_number')
    website = factory.Faker('url')
    socials = [
        {
            'url': 'https://example.com',
            'icon': 'https://logo.com'
        } for _ in range(3)
    ]

    location = factory.SubFactory(LocationFactory)
