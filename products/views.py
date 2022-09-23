from django.shortcuts import render
from rest_framework import generics , permissions
from .models import Product
from .serializers import ProductSerializers
# from .permissions import IsUserPermissions


class ProductListCreate(generics.ListCreateAPIView):
    queryset = Product.objects.active_product()
    serializer_class = ProductSerializers
    permission_classes = [permissions.IsAuthenticated]

product_list_create = ProductListCreate.as_view()



class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.active_product()
    serializer_class = ProductSerializers
    permission_classes = [permissions.IsAuthenticated]


product_detail_view = ProductDetailView.as_view()




