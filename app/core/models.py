from django.db import models

# Create your models here.


class Product(models.Model):
    """Model of Product"""
    code = models.CharField(max_length=6, primary_key=True)
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return self.name


class Basket(models.Model):
    """Model of Basket"""


class BasketItem(models.Model):
    """Model for item inside in basket"""

    basket = models.ForeignKey(
        Basket,
        related_name='products',
        on_delete=models.CASCADE,
    )

    product = models.ForeignKey(
        Product,
        related_name='products',
        on_delete=models.CASCADE,
    )

    qty = models.PositiveIntegerField(default=1, null=True, blank=True)

    def __str__(self):
        return "{0}:{1}".format(self.product.code, self.qty)
