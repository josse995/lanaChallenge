from django.urls import path


from django.urls import path, include
from rest_framework.routers import DefaultRouter

from shop import views

router = DefaultRouter()
router.register('list', views.ProductViewSet)
router.register('buy', views.BasketViewSet)

app_name = 'shop'

urlpatterns = [
    path('', include(router.urls)),
]
