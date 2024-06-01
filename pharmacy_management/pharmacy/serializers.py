from rest_framework import serializers
from .models import Medicine, MedicalSupply

class MedicineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medicine
        fields = '__all__'

class MedicalSupplySerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicalSupply
        fields = '__all__'