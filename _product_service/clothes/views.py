from rest_framework import viewsets
from .models import Clothes, Style, Producer
from .serializers import ClothesSerializer, StyleSerializer, ProducerSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

class ClothesViewSet(viewsets.ModelViewSet):
    queryset = Clothes.objects.all()
    serializer_class = ClothesSerializer

class StyleViewSet(viewsets.ModelViewSet):
    queryset =  Style.objects.all()
    serializer_class = StyleSerializer

class ProducerViewSet(viewsets.ModelViewSet):
    queryset = Producer.objects.all()
    serializer_class = ProducerSerializer

@api_view(['GET'])
def view_clothes_by_id(request, id):
    try:
        clothes = Clothes.objects.get(id=id)
    except Clothes.DoesNotExist:
        return Response({'error': 'Clothes not found'}, status=status.HTTP_404_NOT_FOUND)
    serializer = ClothesSerializer(clothes)
    return Response(serializer.data)

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
