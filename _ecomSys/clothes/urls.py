from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'clothes', views.ClothesViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('add_to_cart/', views.add_clothes_to_cart, name='add-clothes-to-cart'),
]

