from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'api/clothes/', views.ClothesViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api/search/', views.search_clothes, name='search_clothes'),
]
