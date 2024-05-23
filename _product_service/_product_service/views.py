from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse


@api_view(['GET'])
def api_root(request, format=None):

    return Response({
        'mobiles': reverse('mobile-list', request=request, format=format),
        'clothes': reverse('clothes-list', request=request, format=format),
        'books': reverse('book-list', request=request, format=format),
    })