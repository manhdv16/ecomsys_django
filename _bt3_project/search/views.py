from django.shortcuts import render
from .forms import SearchForm
from book.models import Book
from mobile.models import Mobile

def search(request):
    form = SearchForm()
    context = {'form': form}
    if 'query' in request.GET:
        query = request.GET['query']
        books = Book.objects.filter(title=query)
        mobiles = Mobile.objects.filter(model_name=query)
        context['books'] = books
        context['mobiles'] = mobiles
    return render(request, 'search.html', context)
