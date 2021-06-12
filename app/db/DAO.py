from app.model.product import Product
from app.helpers.singleton import Singleton
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.db import constants


class DAO(metaclass=Singleton):
    """Class to manage the connection with DB"""

    def __init__(self):
        engine = create_engine(
            'postgresql://{root}:{password}@{ip}:{port}/{database}'.format(
                root=constants.POSTGRES_USER,
                password=constants.POSTGRES_PASSWORD,
                ip=constants.POSTGRES_IPADDRESS,
                port=constants.POSTGRES_PORT,
                database=constants.POSTGRES_DATABASE))
        Session = sessionmaker(engine)
        self.session = Session()

    def getProductByCode(self, code):
        """Retrieve the product with a code giving"""
        queryResult = self.session.query(Product).filter(
            Product.code == code.strip()
        )
        # We are searching by code, which it is PK, so we expect no more than one result
        if(queryResult.count() == 1):
            return queryResult[0]
        else:
            return None


if __name__ == '__main__':
    conn = DAO()
