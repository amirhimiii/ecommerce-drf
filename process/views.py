from django.shortcuts import render
from rest_framework import generics
from django.shortcuts import render, redirect, get_object_or_404

class AddProductToCart(generics.CreateAPIView):
    def get_queryset(self):
        return super().get_queryset()
    



