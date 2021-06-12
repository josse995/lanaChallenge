from app.helpers.singleton import Singleton
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class Connection(metaclass=Singleton):
    """Class to manage the connection with DB"""

    def __init__(self):
        engine = create_engine('postgresql://root:password@localhost/docker')
        Session = sessionmaker(engine)
        self.session = Session()


if __name__ == '__main__':
    conn = Connection()
