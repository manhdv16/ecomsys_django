from django.db import models

class Payment(models.Model):
    order_id = models.PositiveIntegerField()
    user_id = models.PositiveIntegerField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=50, default='Pending')
