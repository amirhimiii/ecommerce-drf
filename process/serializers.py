from rest_framework import serializers
from .models import Cart , CartItem, Checkout
from rest_framework.response import Response
from profiles.serializers import UserList
from django_countries.serializer_fields import CountryField
from django_countries.serializers import CountryFieldMixin
from accounts.models import CustomUser
from phonenumber_field.serializerfields import PhoneNumberField


#POST Serializer
class CartItemSerializers(serializers.ModelSerializer):
    cart = serializers.CharField(source="cart.user", read_only=True)

    class Meta:
        model = CartItem
        fields = ['cart','product','quantity']
        read_only_fields = ['cart']



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
    





class CheckoutSerializer(CountryFieldMixin ,serializers.ModelSerializer):
    phone_number = PhoneNumberField(region="IR")
    country = CountryField()
    email = serializers.ReadOnlyField()
    cart=serializers.StringRelatedField()
    user= serializers.StringRelatedField()
    zip_code = serializers.IntegerField(max_value=9, min_value=5)

    class Meta:
        model = Checkout
        exclude = ['id']

    def get_phone_number(self, obj):
        return obj.phone_number()