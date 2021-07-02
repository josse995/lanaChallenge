
from django.forms import fields
from rest_framework import viewsets, status
from rest_framework.decorators import action, detail_route, permission_classes
from rest_framework.response import Response
from rest_framework import permissions
from core.models import Product, Basket, BasketItem
from shop import serializers

import decimal


class ProductViewSet(viewsets.ModelViewSet):
    """Viewset for prodcuts"""

    queryset = Product.objects.all()
    serializer_class = serializers.ProductSerializer


class BasketViewSet(viewsets.ModelViewSet):
    """Viewset for Basket"""
    queryset = Basket.objects.all()
    serializer_class = serializers.BasketSerializer

    @action(detail=False, methods=['post'])
    def add(self, request, **kwargs):
        """Add to the basket (with basketId) the given product (with product code)"""
        basketId = request.data.get('basket')
        if not basketId:
            return Response(data={'error': 'BasketId is missing.'}, status=status.HTTP_400_BAD_REQUEST)

        basket = Basket.objects.filter(id=basketId).first()
        if not basket:
            return Response(data={'error': 'The basket with id {0} not found on database.'
                                  .format(basketId)}, status=status.HTTP_400_BAD_REQUEST)

        productCode = request.data.get('product')
        if not productCode:
            return Response(data={'error': 'Product code is not provided.'}, status=status.HTTP_400_BAD_REQUEST)
        product = Product.objects.filter(code=productCode).first()
        if not product:
            return Response(data={'error': 'The product with code {0} not found on database.'
                                  .format(productCode)}, status=status.HTTP_400_BAD_REQUEST)

        basketItem = BasketItem.objects.filter(
            basket=basket, product=product).first()
        if basketItem:
            basketItem.qty += 1
        else:
            basketItem = BasketItem(basket=basket, product=product)

        basketItem.save()
        serializer = serializers.BasketSerializer(basket)
        return Response(serializer.data)

    @action(detail=False)
    def checkout(self, request, **kwargs):
        """Endpoint that calculates all the total price of a given basket"""
        basketId = request.query_params.get('basket')
        if not basketId:
            return Response(data={'error': 'BasketId is missing.'}, status=status.HTTP_400_BAD_REQUEST)

        basket = Basket.objects.filter(id=basketId).first()
        if not basket:
            return Response(data={'error': 'Basket with id {0} is not found on database.'.format(basketId)},
                            status=status.HTTP_400_BAD_REQUEST)

        total = 0.00

        for basketItem in basket.products.all():
            discount = 0.00
            product = basketItem.product
            if(product.code == 'PEN'):
                qtyFree = basketItem.qty // 2
                discount = product.price * qtyFree
            elif(product.code == 'TSHIRT'):
                if(basketItem.qty >= 3):
                    discount = 0.25 * product.price * basketItem.qty
            total += product.price * basketItem.qty - discount

        return Response({'total': '{0}{1}'.format(decimal.Decimal('{0:.2f}'.format(total)), '€')}, status=status.HTTP_200_OK)
