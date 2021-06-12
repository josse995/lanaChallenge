from app.db.DAO import DAO
from app.model.product import Product
import sys
import os
sys.path.insert(0, os.getcwd())

if __name__ == '__main__':
    conn = DAO()

    finish = False
    while(not finish):
        text = input("Introduce the productos (0 for exit): ")
        if(text == '0'):
            finish = True
        else:
            pass
