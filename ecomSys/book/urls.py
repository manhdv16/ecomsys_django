from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
from .views import add_book_to_cart

router = DefaultRouter()
router.register(r'', views.BookViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('add_to_cart/', add_book_to_cart, name='add-book-to-cart'),
]
