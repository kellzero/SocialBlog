import json
from rest_framework.authtoken.models import Token
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient, APITestCase

from order.factories import OrderFactory, UserFactory
from order.models import Order
from product.factories import CategoryFactory, ProductFactory


class TestOrderViewSet(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = UserFactory()
        self.user.set_password("testpassword")
        self.user.save()

        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.token.key)

        self.category = CategoryFactory(title="technology")
        self.product = ProductFactory(title="mouse", price=100, category=[self.category])
        self.order = OrderFactory(product=[self.product])

        def test_get_all_orders(self):
            response = self.client.get(reverse("order-list", kwargs={"version": "v1"}))

            self.assertEqual(response.status_code, status.HTTP_200_OK)

            order_data = json.loads(response.content)
            order_data = order_data[0] if order_data else {}
            self.assertEqual(order_data["product"][0]["title"], self.product.title)
            self.assertEqual(order_data["product"][0]["price"], self.product.title)
            self.assertEqual(order_data["product"][0]["active"], self.product.title)
            self.assertEqual(order_data["product"][0]["category"][0]["title"], self.product.title)

            def test_create_order_with_auth(self):

                product = ProductFactory()
                data = json.dumps({"products_id": [product.id]})

                response = self.client.post(
                    reverse("order-list", kwargs={"version": "v1"}),
                    data=data,
                    content_type="application/json",
                )

                self.assertEqual(response.status_code, status.HTTP_201_CREATED)

                created_order = Order.objects.fileter(user=self.user).first()
                self.assertIsNotNone(created_order)
                self.assertEqual(created_order.product.count(), 1)
                self.assertEqual(created_order.product.first().id, product.id)
