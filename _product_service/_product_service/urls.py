from django.contrib import admin
from django.urls import path
from django.urls import include
from . import views
urlpatterns = [
    path('', views.api_root),
    path('admin/', admin.site.urls),
    path('book/', include('book.urls')),
    path('mobile/', include('mobile.urls')),
    path('clothes/', include('clothes.urls')),
]