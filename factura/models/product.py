from django.db import models

class Product(models.Model):
    id_product = models.AutoField(primary_key=True)
    product_name = models.CharField('Product Name', max_length=30)
    product_stock = models.IntegerField(default=0)
    product_price = models.IntegerField(default=0)
    isActive = models.BooleanField(default=True)