import factory
from factory import SubFactory

from .category_type import CategoryTypeFactory
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
    language = 'en'
    translated_languages = ['en']

    parent = None
    type = SubFactory(CategoryTypeFactory)

    @factory.post_generation
    def children(self, create, extracted, **_):
        if not create:
            return

        if extracted:
            for child in extracted:
                self.children.append(child)
