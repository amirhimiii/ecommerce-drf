from django.urls import path
from . import views

urlpatterns = [
    path('cartitem/', views.cart_item ,name='add_to_cart'),
    path('cart/<int:pk>', views.detail_update_view ,name='add_to_cart'),
    path('checkout/', views.checkout_view ,name='checkout'),

]

