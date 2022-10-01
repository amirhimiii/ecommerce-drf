from django.shortcuts import render
from rest_framework import generics, permissions, viewsets
from django.contrib.auth import get_user_model
from .serializers import UserList, UserDetail
from .permissions import StaffUserPermissions, IsSuperUserOrStaffPermissions




User = get_user_model()
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserList

    def get_permissions(self):
        if self.action in ['list','create','update']:
            permission_classes = [StaffUserPermissions]
        else:
            permission_classes = [IsSuperUserOrStaffPermissions]
        return [permission() for permission in permission_classes]