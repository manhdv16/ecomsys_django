from django.urls import path, include
from rest_framework import routers
from .views import MobileViewSet, TypeViewSet
from . import views
router = routers.DefaultRouter()
router.register(r'api/mobile', MobileViewSet)
router.register(r'api/types', TypeViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api/search/', views.search_mobile, name='search_mobile'),
]
