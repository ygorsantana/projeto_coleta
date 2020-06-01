from rest_framework import serializers

# from core.models import Product, Store, Sku, Shopping
from core.models import Pessoa

# class ProductSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Product
#         fields = '__all__'
#         depth = 1


# class StoreSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Store
#         fields = '__all__'
#         depth = 1


# class SkuSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Sku
#         fields = '__all__'
#         depth = 1


# class ShoppingSerializer(object):
#     class Meta:
#         model = Shopping
#         fields = '__all__'
#         depth = 1


class PessoaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pessoa
        fields = '__all__'
        depth = 1


class HomeListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pessoa
        fields = [
            'pontuacao'
        ]