from django.shortcuts import render, redirect, get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from products.models import Product
from .models import Cart , CartItem
from .serializers import CartItemSerializers, CartSerializers, CartItemShowSerializers
from rest_framework.exceptions import NotAcceptable, ValidationError, PermissionDenied
from rest_framework import permissions, status
from django.core.exceptions import ObjectDoesNotExist
from django.utils import timezone
from rest_framework import permissions
import datetime

now = datetime.datetime.now()





class CartItemAPIView(APIView):
    serializer_class = CartItemSerializers
    permissions_classes = (permissions.IsAdminUser)

    def post(self ,request, *args, **kwargs):
        user = request.user
        product = get_object_or_404(Product, pk=request.data["product"])        
        
        try:
            cart = Cart.objects.get(user=user)
        except ObjectDoesNotExist:
            cart = Cart.objects.create(user=user, status='NP',ordered=True, date_paid=timezone.now())
        try:
            quantity = int(request.data["quantity"])
        except Exception as e:
            raise ValidationError("Please Enter Your Quantity")
        
        if user == product.user:
            raise PermissionDenied("This Is Your Product")
        
        current_item = CartItem.objects.filter(cart=cart, product=product)
        if current_item.count() > 0:
            raise NotAcceptable("You already have this item in your shopping cart")

        cart_item = CartItem(cart=cart, product=product, quantity=quantity)
        cart_item.save()
        serializer = CartItemSerializers(cart_item)
        return Response(serializer.data)
    
    def get(self , request):
        user = self.request.user
        if self.request.user.is_authenticated:
            cart= Cart.objects.filter(user=user).first()
        else:    
            raise PermissionDenied("you must login")
        cart= Cart.objects.filter(user=user).first()
        cart_item = CartItem.objects.filter(cart=cart)
        serializer = CartItemShowSerializers(cart_item, many=True)
        return Response(serializer.data )




cart_item = CartItemAPIView.as_view()




class RetrieveUpdateDestroy(APIView):
    serializer_class = CartSerializers
    permissions_classes = (permissions.IsAdminUser)
    
    def get(self, request, pk):
        permissions_classes = (permissions.IsAdminUser)
        user = request.user
        if self.request.user.is_authenticated:
            queryset = Cart.objects.filter(user=user )
        else:    
            raise PermissionDenied("you must login")

        serializer = CartSerializers(queryset, many=True)
        return Response(serializer.data)


    def put(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)
        if not pk:
            return Response({'error':'method /PUT/ not allowed'})
        
        try:
            instance = Cart.objects.get(pk=pk , date_paid=timezone.now())
        except:
            return Response({"error":'objects does not exist'})

        serializer = CartSerializers(data=request.data , instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

        

    def delete(self, request, *args, **kwargs):
        user = request.user
        cart = get_object_or_404(Cart, user=user)
        if cart:
            cart.delete()
        return Response({'error':'no cart'})


detail_update_view = RetrieveUpdateDestroy.as_view()