
from core.models import Product, Basket, BasketItem
from rest_framework import serializers


class ProductSerializer(serializers.ModelSerializer):
    """Serializer for the products object"""
    class Meta:
        model = Product
        fields = ('code', 'name', 'price')


class BasketSerializer(serializers.ModelSerializer):
    """Serializer for the basket object"""

    products = serializers.StringRelatedField(many=True)

    class Meta:
        model = Basket
        fields = ('id', 'products',)


class BasketItemSerializer(serializers.Serializer):
    """Serializer for the items inside a basket"""

    basket = BasketSerializer(read_only=True)
    product = ProductSerializer(read_only=True)

    class Meta:
        model = BasketItem
        fields = ('id', 'basket', 'product', 'qty')
