import sys
import os
sys.path.insert(0, os.getcwd())


if __name__ == '__main__':

    from app.db.connection import Connection
    from app.model.product import Product
    #finish = False
    # while(not finish):
    # text = input("Introduce the productos: ")
    # if(not text):
    #     finish = True
    # else:
    conn = Connection()
    products = conn.session.query(Product).all()
    print(*products)
