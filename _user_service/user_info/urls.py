from django.urls import path
from . import views

urlpatterns = [
    path('api/detail/', views.user_detail, name='user_detail'),
]
