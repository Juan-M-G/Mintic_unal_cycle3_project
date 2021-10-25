from factura.models import Bill, Fact_prod, User, Product
from rest_framework import serializers


class BillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bill
        fields = ['id_bill', 'client_name', 'purchase_Date', 'isActive', 'products', 'user_id']
    
    def to_representation(self, obj):
        bill = Bill.objects.get(id_bill=obj.id_bill)
        user = User.objects.get(id=obj.user_id)
        total_bill = 0
        for pro in obj.products:
            product_obj = Product.objects.get(id_product = pro)
            total_bill += product_obj.product_price        
        return {
            'id_factura': bill.id_bill,
            'User': user.username,
            'Client_name': bill.client_name,
            'purchase_Date': bill.purchase_Date,
            'total_bill': total_bill
            }