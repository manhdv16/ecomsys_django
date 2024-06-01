from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'', views.BookViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api/search/', views.search_book_by_keyword, name='search-book-by-keyword')
]
