import factory
from product.models import Product, Category


class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Category

    title = factory.Faker("word")
    slug = factory.Faker("slug")
    description = factory.Faker("sentence")


class ProductFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Product

    title = factory.Faker("word")
    description = factory.Faker("sentence")
    price = factory.Faker(
        "pyint", min_value=1, max_value=1000
    )  # For PositiveBigIntegerField
    activate = factory.Faker("boolean")  # Note: field name is 'activate', not 'active'

    @factory.post_generation
    def category(self, create, extracted, **kwargs):
        if not create:
            return

        if extracted:
            # Add the categories if provided
            for cat in extracted:
                self.category.add(cat)
        else:
            # Add a default category if none provided
            self.category.add(CategoryFactory())
