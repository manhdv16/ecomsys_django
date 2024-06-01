from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AppointmentViewSet, addAppointment

router = DefaultRouter()
router.register(r'appointments', AppointmentViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('addAppointment/', addAppointment),
]
