from rest_framework import viewsets
from .models import Invoice, Payment
from .serializers import InvoiceSerializer, PaymentSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
import requests
from datetime import datetime

class InvoiceViewSet(viewsets.ModelViewSet):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer

class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer

@api_view(['POST'])
def addInvoice(request):
    patient_id = request.data.get('patient_id')
    response = requests.get(f'http://localhost:8002/api/patients/{patient_id}')
    if response.status_code != 200:
        return Response({"message": "Patient not found."}, status=status.HTTP_404_NOT_FOUND)
    totalAmount = request.data.get('totalAmount')
    isPaid = false
    date = datetime.now()
    invoice = Invoice(patient_id=patient_id, totalAmount=totalAmount, isPaid=isPaid, date=date)
    invoice.save()
    return Response({"message": "invoice added successfully."}, status=status.HTTP_201_CREATED)

@api_view(['POST'])
def addPayment(request):
    invoice_id = request.data.get('invoice_id')
    response = requests.get(f'http://localhost:8003/api/invoices/{invoice_id}')
    if response.status_code != 200:
        return Response({"message": "Patient not found."}, status=status.HTTP_404_NOT_FOUND)
    totalAmount = request.data.get('totalAmount')
    isPaid = false
    date = datetime.now()
    payment_method = request.data.get('payment_method')
    payment = Payment(invoice_id=invoice_id, totalAmount=totalAmount, date=date, payment_method=payment_method)
    payment.save()
    invoice = response.json()
    invoice.isPaid = true
    invoice.save()
    return Response({"message": "payment added successfully."}, status=status.HTTP_201_CREATED)