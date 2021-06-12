from sqlalchemy.sql.expression import null
from app.model.product import Product
from app.db.DAO import DAO
import unittest
import psycopg2


class TestMethods(unittest.TestCase):

    def test_connectionDB(self):
        """Test that checks the connection with database"""
        try:
            conn = psycopg2.connect(
                "dbname='docker' user='root' host='localhost' password='password' connect_timeout=1")
            conn.close()
        except:
            print("Error while connecting database...")

        self.assertTrue(conn)

    def test_initializationDB(self):
        """Test that checks if the DB has all the necessary data"""
        dao = DAO()
        productsDB = dao.session.query(Product).all()

        product1 = Product(code='PEN', name='Lana Pen', price=5.00)
        product2 = Product(code='TSHIRT', name='Lana T-Shirt', price=20.00)
        product3 = Product(code='MUG', name='Lana Coffee Mug', price=7.50)

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
        product = Product(code='PEN', name='Lana Pen', price=5.00)
        basket = Basket()

        self.assertTrue(basket.len() == 0)

        basket.addProduct(product)
        self.assertTrue(basket.len() == 1)


if __name__ == '__main__':
    unittest.main()
