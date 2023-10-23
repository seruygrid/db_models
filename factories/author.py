import factory

from .image import ImageFactory
from .base import BaseFactory
from ..db_models import Author


class AuthorFactory(BaseFactory):
    class Meta:
        model = Author
        sqlalchemy_session_persistence = 'commit'

    name = factory.Faker('name')
    is_approved = factory.Faker('pybool')
    slug = factory.Faker('slug')
    bio = factory.Faker('paragraph')
    quote = factory.Faker('sentence')
    born = factory.Faker('date_of_birth')
    products_count = factory.Faker('pyint', min_value=0)
    translated_languages = ['en']
    languages = 'en'
    language = 'en'

    image = factory.SubFactory(ImageFactory)
    cover_image = factory.SubFactory(ImageFactory)
