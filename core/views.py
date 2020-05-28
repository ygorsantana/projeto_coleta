from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

from core.models import Pessoa
from core.serializers import PessoaSerializer
# from core.models import Product, Sku, Store
# from core.serializers import ProductSerializer, SkuSerializer, StoreSerializer, ShoppingSerializer


# class ProductViewSet(viewsets.ModelViewSet):
#     serializer_class = ProductSerializer

#     def get_queryset(self):
#         return self.request.user.allowed_products()


# class SkuViewSet(viewsets.ModelViewSet):
#     serializer_class = SkuSerializer

#     def get_queryset(self):
#         return self.request.user.allowed_skus()


# class StoreViewSet(viewsets.ModelViewSet):
#     serializer_class = StoreSerializer

#     def get_queryset(self):
#         return self.request.user.allowed_stores()


# class ShoppingViewSet(viewsets.ModelViewSet):
#     serializer_class = ShoppingSerializer

#     def get_queryset(self):
#         return self.request.user.allowed_shoppings()


class PessoaViewSet(viewsets.ModelViewSet):
    serializer_class = PessoaSerializer
    queryset = Pessoa.objects.all()
