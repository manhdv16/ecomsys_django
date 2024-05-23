from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework import viewsets
from .models import Book, Category, Author, Publisher
from .serializers import BookSerializer, CategorySerializer, AuthorSerializer, PublisherSerializer
from rest_framework.response import Response
from rest_framework import status

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class PublisherViewSet(viewsets.ModelViewSet):
    queryset = Publisher.objects.all()
    serializer_class = PublisherSerializer

@api_view(['GET'])
def get_price_book(request, id):
    try:
        book = Book.objects.get(id=id)
        return JsonResponse({'price': book.price})
    except Book.DoesNotExist:
        return JsonResponse({'error': 'Book not found'}, status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def view_book_by_id(request, id):
    try:
        book = Book.objects.get(id=id)
        serializer = BookSerializer(book)
        return Response(serializer.data)
    except Book.DoesNotExist:
        return Response({'error': 'Book not found'}, status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def search_book(request):
    query = request.query_params.get('q', None)
    if query is not None:
        books = Book.objects.filter(title__icontains=query)
        serializer = BookSerializer(books, many=True)
        if len(books) > 0:
            return Response(serializer.data)
        else:
            return Response({'error': 'No books found matching the query'}, 
            status=status.HTTP_404_NOT_FOUND)
    else:
        return Response({'error': 'No query provided'}, status=status.HTTP_400_BAD_REQUEST)
