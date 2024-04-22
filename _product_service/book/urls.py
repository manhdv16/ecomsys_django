from django.urls import path, include
from rest_framework import routers
from .views import BookViewSet, AuthorViewSet, PublisherViewSet, CategoryViewSet
from . import views
router = routers.DefaultRouter()

router.register(r'api/books', BookViewSet)
router.register(r'api/authors', AuthorViewSet)
router.register(r'api/publishers', PublisherViewSet)
router.register(r'api/categories', CategoryViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api/search/', views.search_book, name='search_book'),
]
