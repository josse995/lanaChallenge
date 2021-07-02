from django.urls import path, include
from rest_framework.routers import DefaultRouter

from shop import views

router = DefaultRouter()
router.register('products', views.ProductViewSet)
router.register('basket', views.BasketViewSet)

app_name = 'shop'

urlpatterns = [
    path('', include(router.urls)),
]
