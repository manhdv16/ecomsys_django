from rest_framework import viewsets
from .serializers import BookSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from cart.models import Cart, CartItem
from .models import Book
from django.contrib.contenttypes.models import ContentType

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

@api_view(['POST'])
def add_book_to_cart(request):
    cart_id = request.data.get('cart_id')
    book_id = request.data.get('book_id')
    quantity = request.data.get('quantity', 1)

    try:
        cart = Cart.objects.get(id=cart_id)
    except Cart.DoesNotExist:
        cart = Cart.objects.create()

    try:
        book = Book.objects.get(id=book_id)
    except Book.DoesNotExist:
        return Response({'error': 'Sách không tồn tại'}, status=status.HTTP_404_NOT_FOUND)

    cart_item, created = CartItem.objects.get_or_create(
        cart=cart,
        content_type=ContentType.objects.get_for_model(Book),
        object_id=book_id,
        defaults={'quantity': quantity, 'price': book.price}
    )
    if not created:
        cart_item.quantity += quantity
        cart_item.save()
    return Response({'message': 'Sách đã được thêm vào giỏ hàng'}, status=status.HTTP_201_CREATED)
