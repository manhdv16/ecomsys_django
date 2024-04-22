from djongo import models

class Category(models.Model):
    name = models.CharField(max_length=50, null=True)
    class Meta:
        app_label = 'book'
        db_table='category'

class Author(models.Model):
    name = models.CharField(max_length=100, null=True)
    address = models.CharField(max_length=255, null=True)
    mail = models.EmailField(max_length=100, null=True)
    class Meta:
        app_label = 'book'
        db_table='author'

class Publisher(models.Model):
    name = models.CharField(max_length=100, null=True)
    address = models.CharField(max_length=255, null=True)
    mail = models.EmailField(max_length=100, null=True)
    class Meta:
        app_label = 'book'
        db_table='publisher'
        
class Book(models.Model):
    title = models.CharField(max_length=255,null=True)
    price = models.CharField(max_length=100,null=True)
    image = models.FileField(upload_to='book/images', blank=True, null=True)

    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='books')
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE, related_name='books')
    class Meta:
        app_label = 'book'
        db_table='book'   



