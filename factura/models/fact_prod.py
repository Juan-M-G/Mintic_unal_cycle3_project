from django.db import models
from .bill import Bill
from .product import Product

class Fact_prod(models.Model):
    id_fp = models.AutoField(primary_key=True)
    bill_id = models.ForeignKey(Bill, related_name='fact_prod', on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product, related_name='fact_prod', on_delete=models.CASCADE)
    product_amount = models.IntegerField(default=0)
    sub_total_price = models.IntegerField(default=0)

