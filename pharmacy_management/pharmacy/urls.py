from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MedicineViewSet, MedicalSupplyViewSet

router = DefaultRouter()
router.register(r'medicines', MedicineViewSet)
router.register(r'medical-supplies', MedicalSupplyViewSet)
urlpatterns = [
    path('', include(router.urls)),
]
