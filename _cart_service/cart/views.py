from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Cart, CartItem
from .serializers import CartItemSerializer
import requests

@api_view(['GET', 'POST'])
def getUserInfo(request):
    # Lấy token từ header Authorization
    token = request.headers.get('Authorization').split(' ')[1]
    print(token)

    # Tạo header mới để gửi trong request đến user_service
    headers = {'Authorization': f'Token {token}'}

    # Thực hiện request đến user_service và lấy phản hồi
    user_service_response = requests.get('http://localhost:8002/api/user_detail', headers=headers)
    
    # Kiểm tra status code của phản hồi để xử lý các trường hợp lỗi
    if user_service_response.status_code == 200:
        # Nếu thành công, trả về dữ liệu JSON từ user_service
        return Response(user_service_response.json())
    else:
        # Nếu có lỗi, trả về lỗi tương ứng với status code từ user_service
        return Response(user_service_response.json(), status=user_service_response.status_code)

@api_view(['POST'])
# @permission_classes([IsAuthenticated])
def add_to_cart(request):
    user = request.user
    product_type = request.data.get('product_type')
    product_id = request.data.get('product_id')
    quantity = request.data.get('quantity', 1)
    
    cart, created = Cart.objects.get_or_create(user=user)
    cart_item, created = CartItem.objects.get_or_create(cart=cart, product_type=product_type, product_id=product_id)
    cart_item.quantity += quantity
    cart_item.save()
    if created:
        message = "Added to cart successfully."
    else:
        message = "Quantity updated in cart."
    
    return Response({"message": message}, status=status.HTTP_201_CREATED)

@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def view_cart(request):
    user = request.user
    cart, created = Cart.objects.get_or_create(user=user)
    cart_items = CartItem.objects.filter(cart=cart)
    serializer = CartItemSerializer(cart_items, many=True)
    return Response(serializer.data)

@api_view(['DELETE'])
# @permission_classes([IsAuthenticated])
def remove_from_cart(request, item_id):
    try:
        item = CartItem.objects.get(id=item_id)
        item.delete()
        return Response({"message": "Item removed from cart."}, status=status.HTTP_204_NO_CONTENT)
    except CartItem.DoesNotExist:
        return Response({"error": "Item not found in cart."}, status=status.HTTP_404_NOT_FOUND)
