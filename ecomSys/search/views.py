from rest_framework import generics
from rest_framework.response import Response
from book.models import Book
from mobile.models import Mobile
from clothes.models import Clothes
from .serializers import SearchResultSerializer

class SearchView(generics.ListAPIView):
    serializer_class = SearchResultSerializer

    def get_queryset(self):
        query = self.request.query_params.get('q', '')
        book_results = Book.objects.filter(title__icontains=query).values('id', 'title', 'description', 'price')
        mobile_results = Mobile.objects.filter(model_name__icontains=query).values('id', 'model_name', 'description', 'price')
        clothes_results = Clothes.objects.filter(name__icontains=query).values('id', 'name', 'size', 'price')

        # Gộp kết quả từ ba mô hình thành một danh sách
        all_results = []
        for result in book_results:
            result['type'] = 'book'
            all_results.append(result)
        for result in mobile_results:
            result['type'] = 'mobile'
            all_results.append(result)
        for result in clothes_results:
            result['type'] = 'clothes'
            all_results.append(result)

        return all_results

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
