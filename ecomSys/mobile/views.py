from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Mobile
from .serializers import MobileSerializer
from cart.models import Cart, CartItem
from django.contrib.contenttypes.models import ContentType

class MobileViewSet(viewsets.ModelViewSet):
    queryset = Mobile.objects.all()
    serializer_class = MobileSerializer

@api_view(['POST'])
def add_mobile_to_cart(request):
    cart_id = request.data.get('cart_id')
    mobile_id = request.data.get('mobile_id')
    quantity = request.data.get('quantity', 1)
    try:
        cart = Cart.objects.get(id=cart_id)
    except Cart.DoesNotExist:
        cart = Cart.objects.create()

    try:
        mobile = Mobile.objects.get(id=mobile_id)
    except Mobile.DoesNotExist:
        return Response({'error': 'Điện thoại không tồn tại'}, status=status.HTTP_404_NOT_FOUND)

    cart_item, created = CartItem.objects.get_or_create(
        cart=cart,
        content_type=ContentType.objects.get_for_model(Mobile),
        object_id=mobile_id,
        defaults={'quantity': quantity, 'price': mobile.price}
    )
    if not created:
        cart_item.quantity += quantity
        cart_item.save()

    return Response({'message': 'Điện thoại đã được thêm vào giỏ hàng'}, status=status.HTTP_201_CREATED)
