from django.shortcuts import render, redirect, get_object_or_404
from rest_framework import generics
from products.models import Product
from .models import Cart , CartItem
from .serializers import AddToCartSerializers


class AddProductToCart(generics.CreateAPIView):
    serializer_class = AddToCartSerializers
    queryset = CartItem.objects.all()
    def get_queryset(self, slug):
        # product = get_object_or_404(Product, slug)
        
        return super().get_queryset()
    

add_to_product = AddProductToCart.as_view()

