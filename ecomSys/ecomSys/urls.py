from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from user import urls as user_urls
from django.urls import path, include
from . import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', views.api_root),
    path('home/', views.home, name='home'),
    path('book/', include('book.urls')),
    path('mobile/', include('mobile.urls')),
    path('clothes/', include('clothes.urls')),
    path('', include('cart.urls')),
    path('',include('search.urls')),
    path('',include(user_urls)),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
