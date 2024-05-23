from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
import requests

from .models import Order, OrderItem
from .serializers import OrderSerializer

def get_user_id(request):
    user_id = request.session.get('user_id')
    
    if not user_id:
        token = request.headers.get('Authorization').split(' ')[1]
        headers = {'Authorization': f'Token {token}'}
        response = requests.get('http://localhost:8002/user/api/detail', headers=headers)

        if response.status_code != 200:
            return None
        user_data = response.json()
        user_id = user_data.get('user').get('id')
        request.session['user_id'] = user_id
    return user_id
    
@api_view(['POST'])
def place_order(request):
    user_id = get_user_id(request)

    if not user_id:
        return Response({"message": "User ID not found in the response."}, 
        status=status.HTTP_400_BAD_REQUEST)
    
    token = request.headers.get('Authorization').split(' ')[1]
    headers = {'Authorization': f'Token {token}'}
    cart_service_url = f'http://localhost:8000/api/cart/'
    cart_response = requests.get(cart_service_url, headers=headers)
    
    if cart_response.status_code != 200:
        return Response({"message": "Failed to retrieve cart."}, status=status.HTTP_400_BAD_REQUEST)
    
    cart_data = cart_response.json()
    if not cart_data:
        return Response({"message": "Cart is empty."}, status=status.HTTP_400_BAD_REQUEST)
    
    order = Order(user_id=user_id)
    order.save()
    
    for item in cart_data:
        OrderItem.objects.create(
            order=order,
            product_type=item['product_type'],
            product_id=item['product_id'],
            quantity=item['quantity']
        )
    
    shipment_service_url = 'http://localhost:8004/api/shipment/'
    shipment_payload = {
        'order_id': order.id,
        'user_id': user_id,
        'address': '123 Main St, Springfield, IL 62701',
        'status': 'Pending',
    }
    shipment_response = requests.post(shipment_service_url, json=shipment_payload)
    
    if shipment_response.status_code != 201:
        order.delete()
        return Response({"message": "Failed to create shipment."}, status=status.HTTP_400_BAD_REQUEST)
    
    payment_service_url = 'http://localhost:8005/api/payment/'
    payment_payload = {
        'order_id': order.id,
        'user_id': user_id,
        'amount': calculate_order_total(cart_data)
    }
    payment_response = requests.post(payment_service_url, json=payment_payload)
    
    if payment_response.status_code != 201:
        order.delete()
        return Response({"message": "Payment processing failed."}, status=status.HTTP_400_BAD_REQUEST)
    
    serializer = OrderSerializer(order)
    return Response(serializer.data, status=status.HTTP_201_CREATED)

def calculate_order_total(cart_items):
    total = 0
    for item in cart_items:
        total += item['quantity'] * get_product_price(item['product_type'], item['product_id'])
    return total

def get_product_price(product_type, product_id):
    response = requests.get(f'http://localhost:8001/{product_type}/api/price/{product_id}')
    data = response.json()
    price = float(data.get('price'))
    return price
