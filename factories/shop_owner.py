import factory

from .base import BaseFactory
from .owner_profile import OwnerProfileFactory
from ..db_models import ShopOwner


class ShopOwnerFactory(BaseFactory):
    class Meta:
        model = ShopOwner
        sqlalchemy_session_persistence = 'commit'

    name = factory.Faker('name')
    email = factory.Faker('email')
    email_verified_at = factory.Faker('date_object')
    is_active = factory.Faker('pybool')

    profile = factory.SubFactory(OwnerProfileFactory)
