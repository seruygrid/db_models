import factory

from ..db_models import Type
from .base import BaseFactory


class TypeFactory(BaseFactory):
    class Meta:
        model = Type
        sqlalchemy_session_persistence = 'commit'

    name = factory.Faker('word')
    slug = factory.Faker('slug')
    icon = factory.Faker('uri')
    language = 'en'
    translated_languages = ['en']
    settings = {
        'isHome': True,
        'layoutType': 'base',
        'productCard': 'base',
    }
