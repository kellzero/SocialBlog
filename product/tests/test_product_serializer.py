import pytest

from product.serializers import ProductSerializer


@pytest.mark.django_db
def test_product_serializer():
    data = {
        "title": "Teste serializer",
        "description": "Testando o serializer",
        "price": 999,
        "activate": True,
        "category": [],  # Adicione category como lista vazia
    }

    serializer = ProductSerializer(data=data)
    assert serializer.is_valid(), f"Erros: {serializer.errors}"

    # Test saving the serializer
    product = serializer.save()
    assert product.id is not None
    assert product.title == data["title"]
    assert product.activate == data["activate"]
