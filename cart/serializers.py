from rest_framework import serializers
from main.models import Cart, Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'title', 'description',
                  'category', 'price', 'author')


class AddProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id',)


class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = ('items',)