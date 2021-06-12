from app.db.DAO import DAO
from app.model.product import Product
from app.model.basket import Basket
import sys
import os
sys.path.insert(0, os.getcwd())

if __name__ == '__main__':
    dao = DAO()

    finish = False
    while(not finish):
        error = False
        text = input("Introduce the products (0 for exit): ")
        if(text == '0'):
            finish = True
        else:
            basket = Basket()
            elems = text.split(',')
            for elem in elems:
                if(elem):
                    product = dao.getProductByCode(elem)
                    if(product):
                        basket.addProduct(product)
                    else:
                        error = True
                        print(
                            "The product {p} is not found on database.".format(p=elem))
                        break
            if(not error):
                total = basket.calculateTotal()
                print("Total: {:.2f}€".format(total))
