from django.urls import path
from . import views

urlpatterns = [
    path('api/payment/', views.process_payment, name='process_payment'),
    path('api/payment/<int:payment_id>/', views.get_payment_status, name='get_payment_status'),
]
