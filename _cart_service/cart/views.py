from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Cart, CartItem
from .serializers import CartItemSerializer
import requests
from django.contrib.auth.models import User

@api_view(['POST'])
def add_to_cart(request):
    user_id = request.session.get('user_id')
    
    if not user_id:
        token = request.headers.get('Authorization').split(' ')[1]
        headers = {'Authorization': f'Token {token}'}
        response = requests.get('http://localhost:8002/user/api/detail', headers=headers)

        if response.status_code != 200:
            return Response({"message": "User authentication failed."}, status=status.HTTP_401_UNAUTHORIZED)
        user_data = response.json()
        user_id = user_data.get('user').get('id')
        request.session['user_id'] = user_id

    if not user_id:
        return Response({"message": "User ID not found in the response."}, 
        status=status.HTTP_400_BAD_REQUEST)
    
    product_type = request.data.get('product_type')
    product_id = request.data.get('product_id')
    quantity = request.data.get('quantity', 1)
    
    if not product_type or not product_id:
        return Response({"message": "Product type and product ID are required."}, 
        status=status.HTTP_400_BAD_REQUEST)
    
    cart, created = Cart.objects.get_or_create(user_id=user_id)
    cart_item, item_created = CartItem.objects.get_or_create(cart=cart, product_type=product_type,
     product_id=product_id)
    if not item_created:
        cart_item.quantity += quantity
    else:
        cart_item.quantity = quantity
    cart_item.save()
    message = "Added to cart successfully." if item_created else "Quantity updated in cart."
    return Response({"message": message}, status=status.HTTP_201_CREATED)

@api_view(['GET'])
def view_cart(request):
    user_id = request.session.get('user_id')
    
    if not user_id:
        token = request.headers.get('Authorization').split(' ')[1]
        headers = {'Authorization': f'Token {token}'}
        response = requests.get('http://localhost:8002/user/api/detail', headers=headers)

        if response.status_code != 200:
            return Response({"message": "User authentication failed."}, status=status.HTTP_401_UNAUTHORIZED)
        user_data = response.json()
        user_id = user_data.get('user').get('id')
        request.session['user_id'] = user_id

    if not user_id:
        return Response({"message": "User ID not found in the response."}, 
        status=status.HTTP_400_BAD_REQUEST)

    cart, created = Cart.objects.get_or_create(user_id=user_id)
    cart_items = CartItem.objects.filter(cart=cart)
    serializer = CartItemSerializer(cart_items, many=True)
    return Response(serializer.data)

@api_view(['DELETE'])
def remove_from_cart(request, item_id):
    try:
        item = CartItem.objects.get(id=item_id)
        item.delete()
        return Response({"message": "Item removed from cart."}, status=status.HTTP_204_NO_CONTENT)
    except CartItem.DoesNotExist:
        return Response({"error": "Item not found in cart."}, status=status.HTTP_404_NOT_FOUND)
