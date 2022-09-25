from django.urls import path
from .views import *

urlpatterns = [
    path('',user_list, name='user-list'),
    path('<int:pk>/detail/',user_detail, name='user-detail')
]