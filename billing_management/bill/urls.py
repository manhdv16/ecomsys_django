from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import InvoiceViewSet, PaymentViewSet, addInvoice, addPayment

router = DefaultRouter()
router.register(r'invoices', InvoiceViewSet)
router.register(r'payments', PaymentViewSet)
urlpatterns = [
    path('', include(router.urls)),
    path('addInvoice/', addInvoice),
    path('addPayment/', addPayment),
]
