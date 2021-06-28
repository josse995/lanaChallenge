
from django.http.response import HttpResponse
from rest_framework import viewsets, mixins
from rest_framework.decorators import action, detail_route
from core.models import Product
from product import serializers


class ProductViewSet(viewsets.GenericViewSet,
                     mixins.ListModelMixin,
                     mixins.CreateModelMixin):
    """Viewset for prodcuts"""

    queryset = Product.objects.all()
    serializer_class = serializers.ProductSerializer
    http_method_names = ['get']
