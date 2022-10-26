from django.shortcuts import render,get_object_or_404
from rest_framework import generics , permissions
from .models import Product
from .serializers import ProductSerializers
from .permissions import AuthorObjectPermissions , IsStaffOrReadOnly


class ProductListCreate(generics.ListCreateAPIView):
    queryset = Product.objects.active_product()
    serializer_class = ProductSerializers
    permission_classes = [IsStaffOrReadOnly]
    filterset_fields = ['active','user','price']
    search_fields = ['title','user__username']

    def perform_create(self, serializer):
        if self.request.user.is_authenticated:
            user = serializer.save(user=self.request.user)
        else:
            user = serializer.save()

product_list_create = ProductListCreate.as_view()



class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.active_product()
    serializer_class = ProductSerializers
    permission_classes = [AuthorObjectPermissions]
 

    

product_detail_view = ProductDetailView.as_view()




