import unittest
import psycopg2


class TestMethods(unittest.TestCase):

    def test_connectionDB(self):
        """Test that check the connection with database"""
        try:
            conn = psycopg2.connect(
                "dbname='docker' user='root' host='localhost' password='password' connect_timeout=1")
            conn.close()
            print("Connected to database successfully")
        except:
            print("Error while connecting database...")

        self.assertTrue(conn)


if __name__ == '__main__':
    unittest.main()
