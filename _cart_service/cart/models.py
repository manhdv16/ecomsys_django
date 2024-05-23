from django.db import models

class Cart(models.Model):
    user_id = models.PositiveIntegerField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, related_name='items', on_delete=models.CASCADE)
    product_type = models.CharField(max_length=50)
    product_id = models.PositiveIntegerField()
    quantity = models.PositiveIntegerField(default=1)
