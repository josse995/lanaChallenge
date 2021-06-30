from django.contrib import admin

from core import models
# Register your models here.
admin.site.register(models.Product)
admin.site.register(models.Basket)
admin.site.register(models.BasketItem)
