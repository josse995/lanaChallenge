from django.test import TestCase

from core.models import Product


class ProductApiTests(TestCase):

    def test_get_products(self):
        """Test that checks if the initial products are being introduced properly"""
        pass

    # def test_calculateTotalWithoutDiscount(self):
    #     """Test that calculates the total of the basket without discount"""
    #     penProduct = Product.objects.get(code='PEN')  # It cost 5.00/unit
    #     mugProduct = Product.objects.get(code='MUG')  # It cost 7.50/unit
    #     tShirtProduct1 = Product.objects.get(
    #         code='TSHIRT')  # It cost 20.00/unit
    #     tShirtProduct2 = Product.objects.get(code='TSHIRT')
    #     basket = Basket()

    #     basket.addProduct(penProduct)
    #     basket.addProduct(mugProduct)
    #     basket.addProduct(tShirtProduct1)
    #     basket.addProduct(tShirtProduct2)

    #     total = basket.calculateTotal()

    #     self.assertEqual(52.50, total)

    # def test_calculateTotalWithDiscountPen(self):
    #     """Test that calculates the total of the basket of pens only"""
    #     penProduct = Product.objects.get(code='PEN')
    #     basket = Basket()

    #     for _ in range(11):
    #         basket.addProduct(penProduct)

    #     total = basket.calculateTotal()
    #     self.assertEqual(30.00, total)

    # def test_calculateTotalWithDiscountTShirt(self):
    #     """Test that calculates the total of the basket of T-shirts only"""
    #     tShirtProduct = Product.objects.get(code='TSHIRT')
    #     basket = Basket()

    #     for _ in range(4):
    #         basket.addProduct(tShirtProduct)

    #     total = basket.calculateTotal()
    #     self.assertEqual(60.00, total)

    # def test_calculateTotal(self):
    #     """Test that calculate the total of basket with mix of products"""

    #     # Items: PEN, TSHIRT, PEN, PEN, MUG, TSHIRT, TSHIRT
    #     # Total: 62.50€
    #     pen = Product.objects.get(code='PEN')  # x3
    #     tshirt = Product.objects.get(code='TSHIRT')  # x3
    #     mug = Product.objects.get(code='MUG')  # x1

    #     basket = Basket()

    #     for _ in range(3):
    #         basket.addProduct(pen)
    #         basket.addProduct(tshirt)
    #     basket.addProduct(mug)

    #     total = basket.calculateTotal()
    #     self.assertEqual(62.50, total)

    # def test_calculateTotalWithInput(self):
    #     """Test that calculate the total of basket with mix of products introduced by console"""
    #     input = "PEN, TSHIRT, PEN, PEN, MUG, TSHIRT, TSHIRT"
    #     dao = DAO()

    #     basket = Basket()
    #     elems = input.split(',')
    #     for elem in elems:
    #         product = dao.getProductByCode(elem)
    #         basket.addProduct(product)

    #     total = basket.calculateTotal()
    #     self.assertEqual(62.50, total)
