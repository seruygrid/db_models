import factory
from factory import SubFactory

from .category import CategoryFactory
from .type import TypeFactory
from .base import BaseFactory
from ..db_models import ChildCategory


class ChildCategoryFactory(BaseFactory):
    class Meta:
        model = ChildCategory
        sqlalchemy_session_persistence = 'commit'

    name = factory.Faker('word')
    slug = factory.Faker('slug')
    icon = factory.Faker('uri')
    details = factory.Faker('paragraph')
    image = []
    language = 'en'
    translated_languages = ['en']

    parent = SubFactory(CategoryFactory)
    type = SubFactory(TypeFactory)
