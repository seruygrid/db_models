import factory

from .author import AuthorFactory
from .product_type import ProductTypeFactory
from .shop import ShopFactory
from .shipping import ShippingFactory
from .image import ImageFactory
from .base import BaseFactory
from ..db_models import Product


class ProductFactory(BaseFactory):
    class Meta:
        model = Product
        sqlalchemy_session_persistence = 'commit'

    name = factory.Faker('word')
    slug = factory.Faker('slug')
    description = factory.Faker('paragraph')
    price = factory.Faker('pyfloat')
    sale_price = factory.Faker('pyfloat')
    min_price = factory.Faker('pyfloat')
    max_price = factory.Faker('pyfloat')
    sku = factory.Faker('pystr')
    quantity = factory.Faker('pyint')
    in_stock = factory.Faker('pybool')
    is_taxable = factory.Faker('pybool')
    height = factory.Faker('pyfloat')
    width = factory.Faker('pyfloat')
    length = factory.Faker('pyfloat')
    is_digital = factory.Faker('pybool')
    is_external = factory.Faker('pybool')
    external_product_url = factory.Faker('uri')
    ratings = factory.Faker('pyfloat')
    total_reviews = factory.Faker('pyint')
    in_wishlist = factory.Faker('pybool')
    my_review = factory.Faker('paragraph')
    external_product_button_text = None
    translated_languages = ['en']
    product_type = 'physical'
    manufacturer_id = None
    blocked_dates = None
    status = 'published'
    language = 'en'
    unit = 'unit'

    image = factory.SubFactory(ImageFactory)
    author = factory.SubFactory(AuthorFactory)
    type = factory.SubFactory(ProductTypeFactory)
    shop = factory.SubFactory(ShopFactory)
    shipping_class = factory.SubFactory(ShippingFactory)

    @factory.post_generation
    def gallery(self, create, extracted, **_):
        if not create:
            return

        if extracted:
            for child in extracted:
                self.gallery.append(child)

    @factory.post_generation
    def categories(self, create, extracted, **_):
        if not create:
            return

        if extracted:
            for child in extracted:
                self.categories.append(child)

    @factory.post_generation
    def child_categories(self, create, extracted, **_):
        if not create:
            return

        if extracted:
            for child in extracted:
                self.child_categories.append(child)

    @factory.post_generation
    def rating_count(self, create, extracted, **_):
        if not create:
            return

        if extracted:
            for child in extracted:
                self.rating_count.append(child)
