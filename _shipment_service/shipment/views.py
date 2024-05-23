from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Shipment
from .serializers import ShipmentSerializer
import requests

@api_view(['POST'])
def create_shipment(request):
    order_id = request.data.get('order_id')
    user_id = request.data.get('user_id')
    address = request.data.get('address')
    status = request.data.get('status', 'Pending')
    shipment_fee = 1000
    created_at = datetime.now()

    shipment = Shipment(order_id=order_id, user_id=user_id,created_at=created_at, address=address, shipment_fee=shipment_fee)
    shipment.save()

    serializer = ShipmentSerializer(shipment)
    return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET'])
def get_shipment(request, shipment_id):
    try:
        shipment = Shipment.objects.get(id=shipment_id)
    except Shipment.DoesNotExist:
        return Response({"message": "Shipment not found"}, status=status.HTTP_404_NOT_FOUND)
    
    serializer = ShipmentSerializer(shipment)
    return Response(serializer.data)

@api_view(['PUT'])
def update_shipment(request, shipment_id):
    try:
        shipment = Shipment.objects.get(id=shipment_id)
    except Shipment.DoesNotExist:
        return Response({"message": "Shipment not found"}, status=status.HTTP_404_NOT_FOUND)
    
    shipment.status = request.data.get('status', shipment.status)
    shipment.address = request.data.get('address', shipment.address)
    shipment.shipment_fee = request.data.get('shipment_fee', shipment.shipment_fee)
    shipment.save()

    serializer = ShipmentSerializer(shipment)
    return Response(serializer.data)

@api_view(['DELETE'])
def delete_shipment(request, shipment_id):
    try:
        shipment = Shipment.objects.get(id=shipment_id)
        shipment.delete()
    except Shipment.DoesNotExist:
        return Response({"message": "Shipment not found"}, status=status.HTTP_404_NOT_FOUND)

    return Response({"message": "Shipment deleted"}, status=status.HTTP_204_NO_CONTENT)
