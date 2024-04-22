from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Clothes
from .serializers import ClothesSerializer
from cart.models import Cart, CartItem
from django.contrib.contenttypes.models import ContentType

class ClothesViewSet(viewsets.ModelViewSet):
    queryset = Clothes.objects.all()
    serializer_class = ClothesSerializer

@api_view(['POST'])
def add_clothes_to_cart(request):
    cart_id = request.data.get('cart_id')
    clothes_id = request.data.get('clothes_id')
    quantity = request.data.get('quantity', 1)
    try:
        cart = Cart.objects.get(id=cart_id)
    except Cart.DoesNotExist:
        cart = Cart.objects.create()

    try:
        clothes = Clothes.objects.get(id=clothes_id)
    except Clothes.DoesNotExist:
        return Response({'error': 'Quần áo không tồn tại'}, status=status.HTTP_404_NOT_FOUND)

    cart_item, created = CartItem.objects.get_or_create(
        cart=cart,
        content_type=ContentType.objects.get_for_model(Clothes),
        object_id=clothes_id,
        defaults={'quantity': quantity, 'price': clothes.price}
    )

    if not created:
        cart_item.quantity += quantity
        cart_item.save()
    return Response({'message': 'Quần áo đã được thêm vào giỏ hàng'}, status=status.HTTP_201_CREATED)
