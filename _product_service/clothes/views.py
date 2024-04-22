from rest_framework import viewsets
from .models import Clothes
from .serializers import ClothesSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

class ClothesViewSet(viewsets.ModelViewSet):
    queryset = Clothes.objects.all()
    serializer_class = ClothesSerializer

@api_view(['GET'])
def search_clothes(request):
    query = request.query_params.get('q', None)
    if query is not None:
        clothes = Clothes.objects.filter(name__icontains=query)
        serializer = ClothesSerializer(clothes, many=True)
        if len(clothes) > 0:
            return Response(serializer.data)
        else:
            return Response({'error': 'No clothes found matching the query'}, status=status.HTTP_404_NOT_FOUND)
    else:
        return Response({'error': 'No query provided'}, status=status.HTTP_400_BAD_REQUEST)
