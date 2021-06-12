from app.db import constants
from app.model.basket import Basket
from sqlalchemy.sql.expression import null
from app.model.product import Product
from app.db.DAO import DAO
import unittest
import psycopg2


def createPenProduct():
    return Product(code='PEN', name='Lana Pen', price=5.00)


def createTShirtProduct():
    return Product(code='TSHIRT', name='Lana T-Shirt', price=20.00)


def createMugProduct():
    return Product(code='MUG', name='Lana Coffee Mug', price=7.50)


class TestMethods(unittest.TestCase):

    def test_connectionDB(self):
        """Test that checks the connection with database"""
        try:
            conn = psycopg2.connect(
                "dbname='{database}' user='{user}' host='{ip}' password='{password}' connect_timeout=1".format(
                    database=constants.POSTGRES_DATABASE,
                    user=constants.POSTGRES_USER,
                    ip=constants.POSTGRES_IPADDRESS,
                    password=constants.POSTGRES_PASSWORD
                ))
            conn.close()
        except:
            print("Error while connecting database...")

        self.assertTrue(conn)

    def test_initializationDB(self):
        """Test that checks if the DB has all the necessary data"""
        dao = DAO()
        productsDB = dao.session.query(Product).all()

        product1 = createPenProduct()
        product2 = createTShirtProduct()
        product3 = createMugProduct()

        self.assertIn(product1, productsDB)
        self.assertIn(product2, productsDB)
        self.assertIn(product3, productsDB)

    def test_getProduct(self):
        """Test that gets the product by user's input"""
        input = 'PEN'
        dao = DAO()

        elems = input.split(',')
        for elem in elems:
            product = dao.getProductByCode(elem)
            self.assertTrue(product)

    def test_addProductToBasket(self):
        """Test that adds a product to the basket"""
        product = createPenProduct()
        basket = Basket()

        self.assertTrue(basket.count() == 0)

        basket.addProduct(product)
        self.assertTrue(basket.count() == 1)

    def test_calculateTotalWithoutDiscount(self):
        """Test that calculates the total of the basket without discount"""
        penProduct = createPenProduct()  # It cost 5.00/unit
        mugProduct = createMugProduct()  # It cost 7.50/unit
        tShirtProduct1 = createTShirtProduct()  # It cost 20.00/unit
        tShirtProduct2 = createTShirtProduct()
        basket = Basket()

        basket.addProduct(penProduct)
        basket.addProduct(mugProduct)
        basket.addProduct(tShirtProduct1)
        basket.addProduct(tShirtProduct2)

        total = basket.calculateTotal()

        self.assertEqual(52.50, total)

    def test_calculateTotalWithDiscountPen(self):
        """Test that calculates the total of the basket of pens only"""
        penProduct = createPenProduct()
        basket = Basket()

        for _ in range(11):
            basket.addProduct(penProduct)

        total = basket.calculateTotal()
        self.assertEqual(30.00, total)

    def test_calculateTotalWithDiscountTShirt(self):
        """Test that calculates the total of the basket of T-shirts only"""
        tShirtProduct = createTShirtProduct()
        basket = Basket()

        for _ in range(4):
            basket.addProduct(tShirtProduct)

        total = basket.calculateTotal()
        self.assertEqual(60.00, total)

    def test_calculateTotal(self):
        """Test that calculate the total of basket with mix of products"""

        # Items: PEN, TSHIRT, PEN, PEN, MUG, TSHIRT, TSHIRT
        # Total: 62.50€
        pen = createPenProduct()  # x3
        tshirt = createTShirtProduct()  # x3
        mug = createMugProduct()  # x1

        basket = Basket()

        for _ in range(3):
            basket.addProduct(pen)
            basket.addProduct(tshirt)
        basket.addProduct(mug)

        total = basket.calculateTotal()
        self.assertEqual(62.50, total)


if __name__ == '__main__':
    unittest.main()
