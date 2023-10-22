import factory

from .base import BaseFactory
from ..db_models import CategoryType


class CategoryTypeFactory(BaseFactory):
    class Meta:
        model = CategoryType
        sqlalchemy_session_persistence = 'commit'

    name = factory.Faker('word')
    language = 'en'
    translated_languages = ['en']
    settings = {}
