from factura.models.bill import Bill
from rest_framework import serializers


class BillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bill
        fields = ['id_bill', 'client_name', 'purchase_Date', 'isActive', 'products', 'user_id']
       