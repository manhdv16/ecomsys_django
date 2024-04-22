from djongo import models

class Clothes(models.Model):

    name = models.CharField(max_length=255)
    image= models.FileField(upload_to='clothes/images', blank=True, null=True)
    brand = models.CharField(max_length=100)
    price = models.CharField(max_length=100,null=True)
    size = models.CharField(max_length=10)
    color = models.CharField(max_length=50)
    gender = models.CharField(max_length=50, choices=[('Men', 'Men'), ('Women', 'Women'), ('Unisex', 'Unisex')])

    class Meta:
        app_label = 'clothes'
        db_table='clothes'
