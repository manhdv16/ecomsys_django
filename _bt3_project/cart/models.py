from django.db import models

class Cart(models.Model):
    session_key = models.CharField(max_length=40, null=True, blank=True)
    class Meta:
        app_label = 'cart'
        db_table='cart'

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    book_title = models.CharField(max_length=255)
    img_url = models.CharField(max_length=255)
    quantity = models.PositiveIntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    class Meta:
        app_label = 'cart'
        db_table='cartitem'