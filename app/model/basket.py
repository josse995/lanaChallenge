
class Basket():
    """Class that contains all the products to buy"""

    def __init__(self):
        self.products = {}

    def count(self):
        return len(self.products)

    def addProduct(self, product):
        """Add a product to the basket"""
        p = self.products.get(product.code)
        if(p):
            self.products[product.code]['qty'] += 1
        else:
            self.products[product.code] = {
                'price': product.price, 'qty': 1}

    def calculateTotal(self):
        """Calculate the total from the basket"""
        total = 0.00
        for product in self.products:
            total += self.__applyDiscountsToProduct(
                product, self.products[product])
        return total

    def __applyDiscountsToProduct(self, productCode, productInfo):
        """Check the basket to apply the discounts"""
        discount = 0.0
        qty = productInfo['qty']
        price = productInfo['price']
        if(productCode == 'PEN'):
            qtyFree = productInfo['qty'] // 2
            discount = productInfo['price'] * qtyFree
        elif(productCode == 'TSHIRT'):
            if(qty >= 3):
                discount = 0.25 * price * qty
        return price * qty - discount
