from django.urls import path
from . import views

urlpatterns = [
    path('api/shipment/', views.create_shipment, name='create_shipment'),
    path('api/shipment/<int:shipment_id>/', views.get_shipment, name='get_shipment'),
    path('api/shipment/update/<int:shipment_id>/', views.update_shipment, name='update_shipment'),
    path('api/shipment/delete/<int:shipment_id>/', views.delete_shipment, name='delete_shipment'),
]
