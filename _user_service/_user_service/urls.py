from django.contrib import admin
from django.urls import path
from django.urls import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', include('user_model.urls')),
    path('user/', include('user_login.urls')),
    path('user/', include('user_info.urls')),
]
