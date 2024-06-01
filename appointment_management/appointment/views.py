from rest_framework import viewsets
from .models import Appointment
from .serializers import AppointmentSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
import requests
from datetime import datetime

class AppointmentViewSet(viewsets.ModelViewSet):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer

@api_view(['POST'])
def addAppointment(request):
    patient_id = request.data.get('patient_id')
    doctor_id = request.data.get('doctor_id')
    response = requests.get(f'http://localhost:8002/api/patients/{patient_id}')
    if response.status_code != 200:
        return Response({"message": "Patient not found."}, status=status.HTTP_404_NOT_FOUND)
    patient_data = response.json()
    
    response = requests.get(f'http://localhost:8001/api/doctors/{doctor_id}')
    if response.status_code != 200:
        return Response({"message": "Doctor not found."}, status=status.HTTP_404_NOT_FOUND)
    doctor_data = response.json()
    date = datetime.now()
    reason = request.data.get('reason')
    appointment = Appointment(patient_id=patient_id, doctor_id=doctor_id, 
    appointment_date=date, reason=reason)
    print(appointment)
    appointment.save()
    return Response({"message": "Appointment added successfully."}, status=status.HTTP_201_CREATED)