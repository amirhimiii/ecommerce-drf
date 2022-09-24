from rest_framework import serializers
from .models import Cart , CartItem

class AddToCartSerializers(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = [
            'order',
            'product',
            'quantity'
        ]