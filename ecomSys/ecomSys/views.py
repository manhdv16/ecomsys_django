from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse

from django.shortcuts import render
from book.models import Book
from mobile.models import Mobile
from clothes.models import Clothes

@api_view(['GET'])
def api_root(request, format=None):

    return Response({
        'mobiles': reverse('mobile-list', request=request, format=format),
        'clothes': reverse('clothes-list', request=request, format=format),
        'books': reverse('book-list', request=request, format=format),
    })


def home(request):
    books = Book.objects.all()[:5]
    mobiles = Mobile.objects.all()[:5]
    clothes = Clothes.objects.all()[:5]
    context = {'books': books, 'mobiles': mobiles, 'clothes': clothes}
    return render(request, 'home.html', context)

