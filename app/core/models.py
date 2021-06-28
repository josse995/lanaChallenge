from django.db import models

# Create your models here.


class Product(models.Model):
    """Model of Product"""
    code = models.CharField(max_length=6, primary_key=True)
    name = models.CharField(max_length=255)
    price = models.FloatField()

    def __str__(self):
        return self.name
