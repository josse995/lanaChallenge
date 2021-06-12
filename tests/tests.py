from app.model.product import Product
from app.db.connection import Connection
import unittest
import psycopg2


class TestMethods(unittest.TestCase):

    def test_connectionDB(self):
        """Test that checks the connection with database"""
        try:
            conn = psycopg2.connect(
                "dbname='docker' user='root' host='localhost' password='password' connect_timeout=1")
            conn.close()
            print("Connected to database successfully")
        except:
            print("Error while connecting database...")

        self.assertTrue(conn)

    def test_initializationDB(self):
        """Test that checks if the DB has all the necessary data"""
        conn = Connection()
        productsDB = conn.session.query(Product).all()

        product1 = Product(code='PEN', name='Lana Pen', price=5.00)
        product2 = Product(code='TSHIRT', name='Lana T-Shirt', price=20.00)
        product3 = Product(code='MUG', name='Lana Coffee Mug', price=7.50)

        self.assertIn(product1, productsDB)
        self.assertIn(product2, productsDB)
        self.assertIn(product3, productsDB)


if __name__ == '__main__':
    unittest.main()