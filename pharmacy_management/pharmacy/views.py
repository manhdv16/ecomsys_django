from rest_framework import viewsets
from .models import Medicine, MedicalSupply
from .serializers import MedicineSerializer, MedicalSupplySerializer

class MedicineViewSet(viewsets.ModelViewSet):
    queryset = Medicine.objects.all()
    serializer_class = MedicineSerializer

class MedicalSupplyViewSet(viewsets.ModelViewSet):
    queryset = MedicalSupply.objects.all()
    serializer_class = MedicalSupplySerializer