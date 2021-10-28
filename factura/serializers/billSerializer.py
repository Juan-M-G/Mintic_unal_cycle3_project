from factura.models import Bill, Fact_prod, User, Product
from rest_framework import serializers


class BillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bill
        fields = ['id_bill', 'client_name', 'purchase_Date', 'isActive', 'products', 'user_id']
    
    #redefine to_representation method to show data on final bill
    def to_representation(self, obj):
        bill = Bill.objects.get(id_bill=obj.id_bill)
        user = User.objects.get(username=obj.user_id)
        prod = Fact_prod.objects.filter(bill_id = obj.id_bill)
        total_bill = 0
        product_list = []
        for pro in range(0, len(prod)):
            prod2 = Product.objects.get(id_product = prod[pro].product_id)
            product_dic = {
                "product_name": prod2.product_name,
                "sub_total_price": prod[pro].product_amount,
                "product_price": prod2.product_price
            }
            product_list.append(product_dic)
            product_obj = prod[pro].sub_total_price
            total_bill += product_obj        
        return {
            'id_factura': bill.id_bill,
            'User': user.id,
            'Client_name': bill.client_name,
            'purchase_Date': bill.purchase_Date,
            'prodcuto': product_list,
            'total_bill': total_bill
            }