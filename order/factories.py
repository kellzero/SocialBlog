import factory
from django.contrib.auth.models import User

from order.models import Order


class UserFactory(factory.django.DjangoModelFactory):
    email = factory.Faker("pystring")
    username = factory.Faker("pystring")

    class Meta:
        model = User


class OrderFactory(factory.django.DjangoModelFactory):
    user = factory.SubFactory(UserFactory)

    @factory.post_generation
    def product(self, create, extracted, **kwargs):
        if not create:
            return
        if extracted:
            for product in extracted:
                self.product.add(product)

    class Meta:
        model = Order
