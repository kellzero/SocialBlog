import pytest
from django.contrib.auth.models import User


@pytest.mark.django_db
def test_create_user():
    user = User.objects.create_user(
        username="d4rk_k1ll4",
        email="dark.killa@bol.com.br",
        password="ilovekittens@777",
        first_name="Oscar",
        last_name="Alho",
    )

    # If you have a UserProfile model with additional fields, create it separately
    # from your_app.models import UserProfile
    # profile = UserProfile.objects.create(
    #     user=user,
    #     country="Brasil",
    #     state="São Paulo",
    #     city="Piraporinha do Leste",
    #     postal_code="12345-789",
    #     address="R. dos Bobos, nº0"
    # )

    assert user.id is not None
    assert user.username == "d4rk_k1ll4"
    assert user.email == "dark.killa@bol.com.br"
