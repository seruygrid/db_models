import factory
from factory import SubFactory

from .type import TypeFactory
from .base import BaseFactory
from ..db_models import Category


class CategoryFactory(BaseFactory):
    class Meta:
        model = Category
        sqlalchemy_session_persistence = 'commit'

    name = factory.Faker('word')
    slug = factory.Faker('slug')
    icon = factory.Faker('uri')
    details = factory.Faker('paragraph')
    image = []
    language = 'en'
    translated_languages = ['en']

    type = SubFactory(TypeFactory)

    @factory.post_generation
    def children(self, create, extracted, **_):
        if not create:
            return

        if extracted:
            for child in extracted:
                self.children.append(child)
