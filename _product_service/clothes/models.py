from djongo import models

class Producer(models.Model):
    name = models.CharField(max_length=255)
    country = models.CharField(max_length=100)
    founded_year = models.IntegerField()
    website = models.URLField(blank=True, null=True)
    class Meta:
        app_label = 'clothes'
        db_table = 'producer'

class Style(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    popular_in_decade = models.CharField(max_length=50, blank=True, null=True)
    class Meta:
        app_label = 'clothes'
        db_table = 'style'

class Clothes(models.Model):
    name = models.CharField(max_length=255)
    image = models.FileField(upload_to='clothes/images', blank=True, null=True)
    brand = models.CharField(max_length=100)
    price = models.CharField(max_length=100, null=True)
    size = models.CharField(max_length=10)
    color = models.CharField(max_length=50)
    producer = models.ForeignKey(Producer, on_delete=models.CASCADE)
    style = models.ForeignKey(Style, on_delete=models.CASCADE)
    class Meta:
        app_label = 'clothes'
        db_table = 'clothes'
