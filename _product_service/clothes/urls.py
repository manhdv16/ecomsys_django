from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import  ClothesViewSet, StyleViewSet, ProducerViewSet
from . import views

router = DefaultRouter()
router.register(r'api/clothes', ClothesViewSet)
router.register(r'api/styles', StyleViewSet)
router.register(r'api/producers', ProducerViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api/search/', views.search_clothes, name='search_clothes'),
]
