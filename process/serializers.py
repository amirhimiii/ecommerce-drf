from rest_framework import serializers
from .models import Cart , CartItem, Checkout
from rest_framework.response import Response
from profiles.serializers import UserList
from products.serializers import ProductSerializers


#POST Serializer
class CartItemSerializers(serializers.ModelSerializer):
    cart = serializers.CharField(source="cart.user", read_only=True)

    class Meta:
        model = CartItem
        fields = ['cart','product','quantity']
        read_only_fields = ['cart']


class TrackListingField(serializers.ModelSerializer):
    def get_queryset(self, obj):
        return self.obj.product.image.url

#Get Serializer
class CartItemShowSerializers(serializers.ModelSerializer):

    image = serializers.SerializerMethodField(source = 'product.image')
    cart = serializers.CharField(source="cart.user", read_only=True)
    product = serializers.CharField(source='product.title')
    price = serializers.SerializerMethodField()
    class Meta:
        model = CartItem
        fields = ['cart','product','quantity','price','image']
        read_only_fields = ['cart']
        # depth= 1

    def get_price(self, obj):
        return obj.price()

    def get_image(self, obj):
        return obj.get_image()

#Shopping Cart
class CartSerializers(serializers.ModelSerializer):
    total_price = serializers.SerializerMethodField()
    class Meta:
        model = Cart
        fields =['status','ordered','date_paid','total_price']
        read_only_fields = ['user']


    def total_price(self, obj):
        return int(obj.total_price)

    
class CheckoutSerializer(serializers.ModelSerializer):
    email = serializers.ReadOnlyField()
    cart=serializers.StringRelatedField()
    user= serializers.StringRelatedField()


    class Meta:
        model = Checkout
        exclude = ['id']

    # def get_serializer_class(self):
    #     if self.request.method == GET:
    #         fields =['__all__']
    #         return fields
    #     exclude = ['cart','user','id','email']
    #     return exclude
