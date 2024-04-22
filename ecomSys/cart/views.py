from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Cart,CartItem
from .serializers import CartSerializer
from .serializers import CartItemSerializer

@api_view(['GET'])
def view_cart(request):
    session_key = request.session.get('cart_id')
    try:
        cart = Cart.objects.get(session_key=session_key)
        serializer = CartSerializer(cart)
        return Response(serializer.data)
    except Cart.DoesNotExist:
        return Response({'error': 'Giỏ hàng không tồn tại'}, status=404)

@api_view(['GET'])
def view_cart_items(request, cart_id):
    try:
        cart = Cart.objects.get(id=cart_id)
        items = CartItem.objects.filter(cart=cart)
        serializer = CartItemSerializer(items, many=True)
        return Response(serializer.data)
    except Cart.DoesNotExist:
        return Response({'error': 'Giỏ hàng không tồn tại'}, status=404)
