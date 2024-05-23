from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Payment
from .serializers import PaymentSerializer
import requests

@api_view(['POST'])
def process_payment(request):
    order_id = request.data.get('order_id')
    user_id = request.data.get('user_id')
    amount = request.data.get('amount')

    payment_status = "Success" if amount > 0 else "Failed"

    payment = Payment(order_id=order_id, user_id=user_id, amount=amount, status=payment_status)
    payment.save()

    serializer = PaymentSerializer(payment)
    return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET'])
def get_payment_status(request, payment_id):
    try:
        payment = Payment.objects.get(id=payment_id)
    except Payment.DoesNotExist:
        return Response({"message": "Payment not found"}, status=status.HTTP_404_NOT_FOUND)
    
    serializer = PaymentSerializer(payment)
    return Response(serializer.data)
