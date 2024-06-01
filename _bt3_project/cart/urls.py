from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_cart, name='view_cart'),
    path('add/<int:book_id>', views.addToCart, name='add_to_cart')
]