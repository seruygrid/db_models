import factory
from factory.alchemy import SQLAlchemyModelFactory


class BaseFactory(SQLAlchemyModelFactory):
    id = factory.Sequence(lambda n: n)
    created_at = factory.Faker('date_object')
    updated_at = factory.Faker('date_object')
