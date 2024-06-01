from djongo import models

class Category(models.Model):
    name = models.CharField(max_length=50, null=True)
    class Meta:
        app_label = 'book'
        db_table='category'

class Book(models.Model):
    title = models.CharField(max_length=255,null=True)
    author = models.CharField(max_length=100,null=True)
    published_date = models.DateField()
    description = models.TextField(blank=True, null=True)
    price = models.CharField(max_length=100,null=True)
    cover_image = models.ImageField(upload_to='book/images', blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='books')

    class Meta:
        app_label = 'book'
        db_table='book'   

