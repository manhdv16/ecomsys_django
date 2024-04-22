from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User

class user_registration(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.CharField(max_length=50)
    mobile = models.CharField(max_length=12)
    password = models.CharField(max_length=50)
    address = models.CharField(max_length=200)
    class Meta:
        app_label = 'user_model'
        db_table='user_registration'
