from django.db import models

class Shipment(models.Model):
    order_id = models.PositiveIntegerField()
    user_id = models.PositiveIntegerField()
    status = models.CharField(max_length=50, default='Pending')
    address = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    shipment_fee = models.DecimalField(max_digits=10, decimal_places=2)
    