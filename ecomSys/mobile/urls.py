from django.urls import path, include
from rest_framework import routers
from .views import MobileViewSet
from .views import add_mobile_to_cart
router = routers.DefaultRouter()
router.register(r'mobiles', MobileViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('add_to_cart/', add_mobile_to_cart, name='add-mobile-to-cart'),
]