from core.models import Product

from rest_framework import serializers


class ProductSerializer(serializers.ModelSerializer):
    """Serializer for the products object"""
    class Meta:
        model = Product
        fields = ('code', 'name', 'price')
