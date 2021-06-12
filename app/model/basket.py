
class Basket():
    """Class that contains all the products to buy"""

    def __init__(self):
        self.products = {}
        self.total = 0

    def count(self):
        return len(self.products)

    def addProduct(self, product):
        """Add a product to the basket"""
        p = self.products.get(product.code)
        if(p):
            self.products[product.code] = p + 1
        else:
            self.products[product.code] = 1
