from django.urls import path
from . import views

urlpatterns = [
    path('api/cart/', views.view_cart, name='view-cart'),
    path('api/cart/add/', views.add_to_cart, name='add-to-cart'),
    path('api/cart/remove/<int:item_id>/', views.remove_from_cart, name='remove-from-cart'),
    path('api/user-info/', views.getUserInfo, name='user-info'),
]

