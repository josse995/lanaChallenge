
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
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

    @action(detail=False)
    def add(self, request, **kwargs):
        basketId = request.query_params.get('basket')
        if not basketId:
            return Response(data={'error': 'BasketId is missing.'}, status=status.HTTP_400_BAD_REQUEST)

        if Basket.objects.filter(id=basketId).exists():
            basket = Basket.objects.get(id=basketId)
        else:
            basket = Basket.objects.create(id=basketId)
            basket.save()

        productCode = request.query_params.get('product')
        if not productCode:
            return Response(data={'error': 'Product code is not provided.'}, status=status.HTTP_400_BAD_REQUEST)
        product = Product.objects.get(code=productCode)
        if not product:
            return Response(data={'error': 'The product with code {1} not found on database.'
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

        return Response({'total': decimal.Decimal('{0:.2f}'.format(total))}, status=status.HTTP_200_OK)
