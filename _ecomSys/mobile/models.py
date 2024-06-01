from djongo import models

class Type(models.Model):
    name = models.CharField(max_length=50, null=True)
    class Meta:
        app_label = 'mobile'
        db_table='type'

class Mobile(models.Model):
    model_name = models.CharField(max_length=255,null=True)
    description = models.TextField(blank=True, null=True)
    price = models.CharField(max_length=100,null=True)
    type = models.ForeignKey(Type, on_delete=models.CASCADE, related_name='mobiles')

    class Meta:
        app_label = 'mobile'
        db_table='mobile'   

