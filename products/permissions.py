from rest_framework import permissions
from rest_framework.permissions import SAFE_METHODS

from accounts.models import CustomUser



# class IsSuperUser(permissions.BasePermission):
#     def has_permission(self, request, view):
#         return bool(request.user.is_superuser)
        

#saff and superuser access
class IsStaffOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        return bool(
            request.method in SAFE_METHODS or
            request.user and request.user.is_staff or request.user.is_authenticated and  request.user.is_author
            )
             

#author access
class AuthorObjectPermissions(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return bool(
            #get access to superuser
            request.user.is_authenticated and request.user.is_superuser or
            #get access to author of obj
            obj.user == request.user
        )




