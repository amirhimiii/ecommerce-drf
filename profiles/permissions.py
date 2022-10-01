from rest_framework import permissions
from rest_framework.permissions import SAFE_METHODS
from products.models import Product


    
#just superuser and staff
class StaffUserPermissions(permissions.BasePermission):
    message = 'just super/staff user'

    def has_permission(self, request,view):
        if request.method in SAFE_METHODS and request.user.is_staff:
            return True
            #get access to superuser
        return bool(request.user.is_superuser)
           




class IsSuperUserOrStaffPermissions(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS and \
        request.user.is_authenticated and request.user.is_staff:
            return True
        return bool(
            #get access to superuser
            request.user.is_superuser
            # obj.id == id
        )




# class ObjectUserPermissions(permissions.BasePermission):
#     def has_object_permission(self, request,view, obj):
#         if obj.user__user == request.user:
#             return True