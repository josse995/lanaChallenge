
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Numeric


Base = declarative_base()

class Product(Base):
  __tablename__ = 'products'

  code = Column(String(10),primary_key=True)
  name = Column(String(), nullable=False)
  price = Column(Numeric(2,10), nullable=False)

  def __str__(self):
    return self.name