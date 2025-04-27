from django.test import TestCase, Client
from django.urls import reverse

class AddToCartIntegrationTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = reverse('add_to_cart')

    def test_add_to_cart(self):
        response = self.client.post(self.url, {
            'id': 2,
            'name': 'swepps agrume',
            'quantity': 1
        })

        self.assertEqual(response.status_code, 302)
        cart = self.client.session['cart']
        self.assertEqual(cart[0]['name'], 'swepps agrume')
        self.assertEqual(cart[0]['quantity'], 1)
