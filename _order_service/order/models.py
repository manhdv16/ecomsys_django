from django.db import models

class Order(models.Model):
    user_id = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    

class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product_type = models.CharField(max_length=50)
    product_id = models.PositiveIntegerField()
    quantity = models.PositiveIntegerField()