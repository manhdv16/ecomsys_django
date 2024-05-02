from django.urls import path
from . import views

urlpatterns = [
    path('api/user_detail/', views.user_detail, name='user_detail'),
]
