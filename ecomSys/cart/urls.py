from django.urls import path
from . import views

urlpatterns = [
    path('api/cart/', views.view_cart, name='view-cart'),
    path('api/cart/<int:cart_id>', views.view_cart_items, name='view-cart-items'),
]

