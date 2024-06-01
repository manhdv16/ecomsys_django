from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RoomViewSet, BedViewSet

router = DefaultRouter()
router.register(r'rooms', RoomViewSet)
router.register(r'beds', BedViewSet)
urlpatterns = [
    path('', include(router.urls)),
]
