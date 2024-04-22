from django.http import JsonResponse
from .models import Mobile, Type
from rest_framework.decorators import api_view
from .serializers import MobileSerializer
from rest_framework import viewsets
from .serializers import TypeSerializer
from rest_framework.response import Response
from rest_framework import status

class MobileViewSet(viewsets.ModelViewSet):
    queryset = Mobile.objects.all()
    serializer_class = MobileSerializer

class TypeViewSet(viewsets.ModelViewSet):
    queryset = Type.objects.all()
    serializer_class = TypeSerializer
    
@api_view(['GET'])
def search_mobile(request):
    query = request.query_params.get('q', None)
    if query is not None:
        mobiles = Mobile.objects.filter(model_name__icontains=query)
        serializer = MobileSerializer(mobiles, many=True)
        if len(mobiles) > 0:
            return Response(serializer.data)
        else:
            return Response({'error': 'No mobiles found matching the query'}, status=status.HTTP_404_NOT_FOUND)
    else:
        return Response({'error': 'No query provided'}, status=status.HTTP_400_BAD_REQUEST)
