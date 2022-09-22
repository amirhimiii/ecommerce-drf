from django.shortcuts import render
from rest_framework import generics



class ProductListCreate(generics.ListCreateAPIView):
    # queryset = 
    # serializer_class = 