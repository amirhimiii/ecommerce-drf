from django.shortcuts import render
from rest_framework import generics , permissions
from .models import Product
from .serializers import ProductSerializers



class ProductListCreate(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers
    permission_classes = [permissions.IsAdminUser
]

product_list_create = ProductListCreate.as_view()



class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers

product_detail_view = ProductDetailView.as_view()




