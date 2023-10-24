import factory
from .models import(
    Product, Person, Passport, Vendor, Shipper,
    ProductsReviews, VendorReviews, ShipperReviews
)


class ProductFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Product

    name = factory.Faker('word')
    description = factory.Faker('sentence')
    price = factory.Faker('pyfloat', positive=True)
    amount = factory.Faker('pyint', min_value=0, max_value=1000)
    category = factory.Faker('random_element', elements=["FR", "VG", "ML", "MT", "TC", "FS", "AL"])


class PersonFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Person

    name = factory.Faker('name')
    address = factory.Faker('address')
    email = factory.Faker('email')
    phone = factory.Faker('phone_number')


class PassportFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Passport

    passport_number = factory.Faker('pyint', min_value=100000, max_value=999999)
    passport_series = factory.Faker('lexify', text='???')


class VendorFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Vendor

    name = factory.Faker('name')
    address = factory.Faker('address')
    email = factory.Faker('email')
    phone = factory.Faker('phone_number')
    inn = factory.Faker('pyint', min_value=100000000, max_value=999999999)


class ShipperFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Shipper

    name = factory.Faker('name')
    address = factory.Faker('address')
    email = factory.Faker('email')
    phone = factory.Faker('phone_number')
    personal_discont = factory.Faker('pyfloat', positive=True)


class ProductsReviewsFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = ProductsReviews

    title = factory.Faker('word')
    description = factory.Faker('text', max_nb_chars=300)
    author = factory.Faker('name')


class VendorReviewsFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = VendorReviews

    title = factory.Faker('word')
    description = factory.Faker('text', max_nb_chars=300)
    author = factory.Faker('name')


class ShipperReviewsFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = ShipperReviews

    title = factory.Faker('word')
    description = factory.Faker('text', max_nb_chars=300)
    author = factory.Faker('name')