from django.urls import path
from . import views

urlpatterns = [
    # path('add_cart/', views.add_to_product ,name='add_to_cart'),
    path('remove_cart/',views.add_to_product, name='remove_from_cart'),
]
