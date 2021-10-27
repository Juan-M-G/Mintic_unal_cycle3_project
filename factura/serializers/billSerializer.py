from factura.models import Bill, Fact_prod, User
from rest_framework import serializers


class BillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bill
        fields = ['id_bill', 'client_name', 'purchase_Date', 'isActive', 'products', 'user_id']
    
    #redefine to_representation method to show a summary of all sells
    def to_representation(self, obj):
        bill = Bill.objects.get(id_bill=obj.id_bill)
        user = User.objects.get(username=obj.user_id)
        prod = Fact_prod.objects.filter(bill_id = obj.id_bill)
        total_bill = 0
        for pro in range(0, len(Fact_prod.objects.filter(bill_id = obj.id_bill))):
            product_obj = prod[pro].sub_total_price
            total_bill += product_obj        
        return {
            'id_factura': bill.id_bill,
            'User': user.id,
            'Client_name': bill.client_name,
            'purchase_Date': bill.purchase_Date,
            'total_bill': total_bill
            }