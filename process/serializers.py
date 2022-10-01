from rest_framework import serializers
from .models import Cart , CartItem

class CartItemSerializers(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = [
            'order',
            'product',
            'quantity'
        ]



class CartSerializers(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = [
            # "user__username",
            "status",
            "ordered",
            "date_paid",
            ]