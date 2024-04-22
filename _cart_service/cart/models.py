from django.db import models
from django.contrib.auth.models import User

class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, related_name='items', on_delete=models.CASCADE)
    product_type = models.CharField(max_length=50)  # Book, Mobile, Clothes
    product_id = models.PositiveIntegerField()
    quantity = models.PositiveIntegerField(default=1)
