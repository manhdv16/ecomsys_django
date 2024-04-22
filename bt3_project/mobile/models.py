from djongo import models

class Brand(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Mobile(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    model_name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    image = models.ImageField(upload_to='mobile/images', null=True, blank=True)

    def __str__(self):
        return f"{self.brand} {self.model_name}"
