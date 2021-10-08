from django.db import models
from .user import User

class Bill(models.Model):
    id_bill = models.AutoField(primary_key=True)
    client_name = models.CharField('Client Name', max_length=30)
    purchase_Date = models.DateTimeField()
    isActive = models.BooleanField(default=True)
    user_id = models.ForeignKey(User, related_name='bill', on_delete=models.CASCADE)