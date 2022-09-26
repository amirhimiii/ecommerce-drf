from rest_framework import permissions
from rest_framework.permissions import SAFE_METHODS

from accounts.models import CustomUser





# class IsSuperOrAthorUser(permissions.BasePermission):

# class IsSuperOrAthorUser(permissions.BasePermission):
#     """
#     The request is authenticated as a user, or is a read-only request.
#     """
#     def has_permission(self, request, view):
#         return bool(
#             request.method in SAFE_METHODS or
#             request.user and
#             request.user.is_superuser or request.user.is_author
#         )

class ObjectPermissions(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return bool(
            request.user.is_authenticated and
            request.user.is_superuser or 
            obj.user == request.user
        )




# class IsUserPermissions(permissions.DjangoModelPermissions):
#     perms_map = {
#         'GET': ['%(app_label)s.view_%(model_name)s'],
#         'OPTIONS': [],
#         'HEAD': [],
#         # 'POST': ['%(app_label)s.add_%(model_name)s'],
#         'PUT': ['%(app_label)s.change_%(model_name)s'],
#         'PATCH': ['%(app_label)s.change_%(model_name)s'],
#         # 'DELETE': ['%(app_label)s.delete_%(model_name)s'],
#     }
    
#     def has_permission(self, request, view):
#         user = request.user
#         if  user.is_superuser:
#             return True

        
        
        # return super().has_permission(request, view)


