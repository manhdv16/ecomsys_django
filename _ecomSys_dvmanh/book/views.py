from rest_framework import viewsets
from .serializers import BookSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Book
from django.contrib.contenttypes.models import ContentType

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

@api_view(['GET'])
def search_book_by_keyword(request):
    query = request.query_params.get('q', '')
    books = Book.objects.filter(title__icontains=query)
    serializer = BookSerializer(books, many=True)
    return Response(serializer.data)