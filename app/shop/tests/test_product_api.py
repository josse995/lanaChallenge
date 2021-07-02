from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from core.models import Product, Basket, BasketItem
from django.urls import reverse

BASKET_URL = reverse('shop:basket-list')
BASKET_URL_ADD = reverse('shop:basket-add')
BASKET_URL_CHECKOUT = '{0}{1}'.format(
    reverse('shop:basket-checkout'), '?basket={0}')


def insert_into_basket_pen_product(basket, qty):
    basketItem = BasketItem.objects.create(
        basket=basket, product=Product.objects.get(code='PEN'))
    basketItem.qty = qty
    basketItem.save()


def insert_into_basket_tshirt_product(basket, qty):
    basketItem = BasketItem.objects.create(
        basket=basket, product=Product.objects.get(code='TSHIRT'))
    basketItem.qty = qty
    basketItem.save()


def insert_into_basket_mug_product(basket, qty):
    basketItem = BasketItem.objects.create(
        basket=basket, product=Product.objects.get(code='MUG'))
    basketItem.qty = qty
    basketItem.save()


class ShopApiTests(TestCase):

    def setUp(self):
        self.client = APIClient()

    # Create basket
    def test_create_basket(self):
        """Test that checks if a basket has been created properly"""
        payload = {}
        res = self.client.post(BASKET_URL, payload)

        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        basket = Basket.objects.get(id=res.data['id'])
        self.assertTrue(basket.products)

    # Delete basket
    def test_delete_basket(self):
        """Test that check if a basket has been deleted properly"""
        basket = Basket.objects.create()
        self.client.delete('{0}{1}/'.format(BASKET_URL, basket.id))
        basket = Basket.objects.filter(id=basket.id).first()
        self.assertFalse(basket)

    # Add to basket
    def test_add_without_parameters(self):
        """Test that executes add without parameters"""
        res = self.client.post(BASKET_URL_ADD, {})

        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_add_to_non_existing_basket(self):
        """Test that adds a product to a non existing basket"""
        payload = {'basket': 0,
                   'product': 'PEN'}

        res = self.client.post(BASKET_URL_ADD, payload)
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_add_non_existing_product_to_a_basket(self):
        """Test that adds a non existing product to a basket"""
        # Creates the basket
        basket = Basket.objects.create()

        payload = {'basket': basket.id,
                   'product': 'NOEXIST'}

        res = self.client.post(BASKET_URL_ADD, payload)
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_add_product_to_a_basket(self):
        """Test that adds a product to a basket"""
        # Creates the basket
        basket = Basket.objects.create()

        payload = {'basket': basket.id,
                   'product': 'PEN'}

        res = self.client.post(BASKET_URL_ADD, payload)
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_add_two_same_prodcuts_to_a_basket(self):
        """Tests that adds a prodcut twice to a basket"""
        # Creates the basket
        basket = Basket.objects.create()

        payload = {'basket': basket.id,
                   'product': 'PEN'}

        # Add the item to the basket twice
        res = self.client.post(BASKET_URL_ADD, payload)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        basket = Basket.objects.get(id=basket.id)
        basketItems = basket.products.all()
        self.assertEqual(basketItems[0].qty, 1)

        res = self.client.post(BASKET_URL_ADD, payload)
        basket.refresh_from_db()
        self.assertEqual(basketItems[0].qty, 2)

    # Checkout
    def test_checkout_example_1(self):
        """Test that retrieve the total of 1 pen, 1 t-shirt and 1 mug"""
        basket = Basket.objects.create()

        insert_into_basket_pen_product(basket, 1)
        insert_into_basket_tshirt_product(basket, 1)
        insert_into_basket_mug_product(basket, 1)

        res = self.client.get(BASKET_URL_CHECKOUT.format(basket.id))
        self.assertEqual(res.data['total'], "32.50€")

    def test_checkout_example_2(self):
        """Test that retrieve the total of 2 pens and 1 t-shirt"""
        basket = Basket.objects.create()

        insert_into_basket_pen_product(basket, 2)
        insert_into_basket_tshirt_product(basket, 1)

        res = self.client.get(BASKET_URL_CHECKOUT.format(basket.id))
        self.assertEqual(res.data['total'], "25.00€")

    def test_checkout_example_3(self):
        """Test that retrieve the total of 4 t-shirts and 1 pen"""
        basket = Basket.objects.create()

        insert_into_basket_tshirt_product(basket, 4)
        insert_into_basket_pen_product(basket, 1)

        res = self.client.get(BASKET_URL_CHECKOUT.format(basket.id))
        self.assertEqual(res.data['total'], "65.00€")

    def test_checkout_example_4(self):
        """Test that retrieve the total of 3 pens, 3 t-shirts and 1 mug"""
        basket = Basket.objects.create()

        insert_into_basket_pen_product(basket, 3)
        insert_into_basket_tshirt_product(basket, 3)
        insert_into_basket_mug_product(basket, 1)

        res = self.client.get(BASKET_URL_CHECKOUT.format(basket.id))
        self.assertEqual(res.data['total'], "62.50€")
