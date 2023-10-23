import factory

from .shop_settings import ShopSettingFactory
from .author import AuthorFactory
from .address import AddressFactory
from .image import ImageFactory
from .base import BaseFactory
from ..db_models import Shop


class ShopFactory(BaseFactory):
    class Meta:
        model = Shop
        sqlalchemy_session_persistence = 'commit'

    name = factory.Faker('company')
    slug = factory.Faker('slug')
    description = factory.Faker('paragraph')
    is_active = factory.Faker('pybool')

    logo = factory.SubFactory(ImageFactory)
    cover_image = factory.SubFactory(ImageFactory)
    owner = factory.SubFactory(AuthorFactory)
    address = factory.SubFactory(AddressFactory)
    settings = factory.SubFactory(ShopSettingFactory)
