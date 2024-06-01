from django.shortcuts import render
from .models import Book, Category
from django.views import View

class HomeView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'index.html')
             

def books(request):
    books = Book.objects.all()
    context = {'books': books}
    return render(request, 'book_list.html', context)


def details(request, id):
    book = Book.objects.get(id=id)
    context = {'book': book}
    return render(request, 'book_detail.html', context)
