import pytest
from product.models import Product


@pytest.mark.django_db
def test_create_product():
    product = Product.objects.create(
        title="Titulo teste do produto",
        description="Descrição de teste",
        price=999,
        activate=True,
    )

    assert product.id is not None
    assert product.title == "Titulo teste do produto"
    assert product.description == "Descrição de teste"
    assert product.price == 999
    assert product.activate == True
