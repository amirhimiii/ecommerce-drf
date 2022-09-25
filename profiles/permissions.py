from rest_framework import permissions
from rest_framework.permissions import SAFE_METHODS
from products.models import Product


class StaffUserPermissions(permissions.BasePermission):
    def has_permission(self, request,view):
        return(
            request.method in SAFE_METHODS and
            request.user and request.user.is_staff or 
            request.user and request.user.is_superuser
        )



# class ObjectUserPermissions(permissions.BasePermission):
#     def has_object_permission(self, request,view, obj):
#         if obj.user__user == request.user:
#             return True