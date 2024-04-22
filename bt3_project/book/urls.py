from django.urls import path
from . import views
from .views import HomeView
urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('book/list/', views.books, name='book_list'),
    path('book/list/details/<int:id>', views.details, name='book_detail'),
]