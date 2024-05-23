from django.urls import path, include
from . import views

urlpatterns = [
    path('api/register/', views.register,  name='register')
]
