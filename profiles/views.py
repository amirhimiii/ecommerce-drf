from django.shortcuts import render
from rest_framework import generics, permissions
from django.contrib.auth import get_user_model
from .serializers import UserList, UserDetail
from .permissions import StaffUserPermissions
# from rest_framework.views import APIView
# from rest_framework.response import Response


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


# class RevokeToken(APIView):
#     permission_classes = [permissions.IsAuthenticated]

#     def delete(self, request):
#         request.auth.delete()
#         return Response(status=204)
    
#     def post(self, reqeust):
#         return Response({"method":"post"})

    # def put(self, request):
    #     return Response({"method":"put"})
    
    # def delete(self, request):
    #     return Response({"method":"delete"})



