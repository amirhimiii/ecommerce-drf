from rest_framework import serializers
from .models import Cart , CartItem
from rest_framework.response import Response
from profiles.serializers import UserList
from products.serializers import ProductSerializers


#POST Serializer
class CartItemSerializers(serializers.ModelSerializer):
    def product_title(self,obj):
        return obj.product.title

    cart = serializers.CharField(source="cart.user", read_only=True)
    product = serializers.SerializerMethodField('get_product')

    class Meta:
        model = CartItem
        fields = ['cart','product','quantity']
        read_only_fields = ['cart']


#Get Serializer
class CartItemShowSerializers(serializers.ModelSerializer):
    cart = serializers.CharField(source="cart.user", read_only=True)
    product = serializers.CharField(source='product.title')
    price = serializers.SerializerMethodField()
    class Meta:
        model = CartItem
        fields = ['cart','product','quantity','price']
        read_only_fields = ['cart']
        # depth= 1

    def get_price(self, obj):
        return obj.price()


#Shopping Cart
class CartSerializers(serializers.ModelSerializer):
    total_price = serializers.SerializerMethodField()
    class Meta:
        model = Cart
        fields =['status','ordered','date_paid','total_price']
        read_only_fields = ['user']


    def total_price(self, obj):
        return int(obj.total_price)