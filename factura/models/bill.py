from django.db import models
from .user import User
from .product import Product

class Bill(models.Model):
    id_bill = models.AutoField(primary_key=True)
    client_name = models.CharField('Client Name', max_length=30)
    purchase_Date = models.DateTimeField()
    isActive = models.BooleanField(default=True)
    products = models.ManyToManyField(Product, related_name= 'products', through= 'Fact_prod')
    user_id = models.ForeignKey(User, related_name='bill', on_delete=models.CASCADE)