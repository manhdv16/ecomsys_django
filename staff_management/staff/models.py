from django.db import models

class Staff(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    role = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    email = models.EmailField()

    def __str__(self):
        return f'{self.first_name} {self.last_name} - {self.role}'
