from django.db import models
from django.contrib.auth.models import User
class UserInfor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    class Meta:
        app_label = 'user'
        db_table='user_infor'