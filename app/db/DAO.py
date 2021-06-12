from app.model.product import Product
from app.helpers.singleton import Singleton
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class DAO(metaclass=Singleton):
    """Class to manage the connection with DB"""

    def __init__(self):
        engine = create_engine('postgresql://root:password@localhost/docker')
        Session = sessionmaker(engine)
        self.session = Session()

    def getProductByCode(self, code):
        """Retrieve the product with a code giving"""
        queryResult = self.session.query(Product).filter(
            Product.code == code.strip()
        )
        # We are searching by code, which it is PK, so we expect no more than one result
        if(queryResult):
            return queryResult[0]
        else:
            return None


if __name__ == '__main__':
    conn = DAO()
