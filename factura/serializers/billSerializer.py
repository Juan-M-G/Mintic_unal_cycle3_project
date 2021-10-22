from factura.models.bill import Bill
from rest_framework import serializers
#from factura.models.fact_prod import Fact_prod
#from factura.serializers.accountSerializer import AccountSerializer

class BillSerializer(serializers.ModelSerializer):
#    fac_prod = AccountSerializer()
    class Meta:
        model = Bill
        fields = ['id_bill', 'client_name', 'purchase_Date', 'isActive', 'products', 'user_id']
        #depth = 1
#        fields = ['id_bill', 'client_name', 'purchase_Date', 'isActive', 'user_id', 'fac_prod']
#    
#    def create(self, validated_data):
#        fact_prodData = validated_data.pop('account')
#        billInstance = Bill.objects.create(**validated_data)
#        Fact_prod.objects.create(bill=billInstance, **fact_prodData)
#        return billInstance
#    def to_representation(self, obj):
#        bill = Bill.objects.get(id=obj.id_bill)
#        fact_prod = Fact_prod.objects.get(bill=obj.id)
#        return {
#            'id_bill': bill.id_bill,
#            'client_name': bill.client_name,
#            'purchase_Date': bill.purchase_Date,
#            'isActive': bill.isActive,
#            'user_id': bill.user_id,
#            'fac_prod': {
#                'id_fp': fact_prod.id_fp,
#                'product_id': fact_prod.product_id,
#                'product_amount': fact_prod.product_amount,
#                'sub_total_price': fact_prod.sub_total_price
#                }
#            }