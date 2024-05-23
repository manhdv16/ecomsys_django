from django.db import models
from django.contrib.auth.models import User

class Account(models.Model):
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    class Meta:
        app_label = 'user_model'
        db_table = 'account'

class Fullname(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    class Meta:
        app_label = 'user_model'
        db_table = 'fullname'

class Address(models.Model):
    commune = models.CharField(max_length=50)
    distrist = models.CharField(max_length=50)  # Ensure correct field name is used
    province = models.CharField(max_length=50)
    class Meta:
        app_label = 'user_model'
        db_table = 'address'

class CustomUser(models.Model):  # Use a unique model name to avoid confusion
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    fullname = models.ForeignKey(Fullname, on_delete=models.CASCADE)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    class Meta:
        app_label = 'user_model'
        db_table = 'user_info'
