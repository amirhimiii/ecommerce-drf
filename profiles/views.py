from django.shortcuts import render
from rest_framework import generics
from django.contrib.auth import get_user_model
from .serializers import UserList, UserDetail
from .permissions import StaffUserPermissions




User = get_user_model()
class ProfileListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserList
    permission_classes = [StaffUserPermissions]

user_list = ProfileListView.as_view()




class ProfileDetailView(generics.RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserDetail
    permission_classes = [StaffUserPermissions]



user_detail = ProfileDetailView.as_view()

