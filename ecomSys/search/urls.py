from django.urls import path
from . import views

urlpatterns = [
    path('search_by_key', views.SearchView.as_view(), name='search'),
]
