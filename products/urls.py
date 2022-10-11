from django.urls import path
from . import views




urlpatterns = [
    path('', views.product_list_create, name='list-create'),
    path('<int:pk>/detail/',views.product_detail_view, name='detail-delete-view'),
]
