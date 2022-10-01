from django.shortcuts import render, redirect, get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets

from rest_framework import generics
from products.models import Product
from .models import Cart , CartItem
from .serializers import CartItemSerializers, CartSerializers
from rest_framework.viewsets import ModelViewSet





