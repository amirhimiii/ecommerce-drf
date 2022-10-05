from rest_framework import serializers
from .models import Cart , CartItem
from rest_framework.response import Response



class CartItemSerializers(serializers.ModelSerializer):
    # product = serializers.CharField(source="product.title")
    cart = serializers.CharField(source="cart.user", read_only=True)
    # product = serializers.PrimaryKeyRelatedField(read_only=True)
    # product = serializers.SerializerMethodField('product')
    # product = serializers.CharField(source='product.title')
    # product_name = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = CartItem
        fields = ['cart','product','quantity']
        read_only_fields = ['cart']
        # depth=1



class CartItemShowSerializers(serializers.ModelSerializer):
    cart = serializers.CharField(source="cart.user", read_only=True)
    # product = serializers.CharField(source="product.title")
    class Meta:
        model = CartItem
        fields = ['cart','product','quantity']
        read_only_fields = ['cart']
        depth= 1



class CartSerializers(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields =['status','ordered','date_paid']
        read_only_fields = ['user']
        depth= 1
