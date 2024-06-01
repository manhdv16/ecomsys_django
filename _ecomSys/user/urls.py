from django.urls import path
from . import views

urlpatterns = [
    path('api/register/', views.register, name='api-register'),
    path('api/login/', views.user_login, name='api-login'),
]

