from rest_framework import status, views
from rest_framework.response import Response
from factura.serializers.billSerializer import BillSerializer
from factura.models import Bill, Product, User, Fact_prod


class BillCreateView(views.APIView):
    #Overwrite post method to add new row Fact_Prod table when there is a new bill 
    def post(self, request, *args, **kwargs):
        #Request data from post 
        data = request.data
        #Create a new row for table Bill
        new_bill = Bill.objects.create(client_name = data['client_name'], purchase_Date = data['purchase_Date'], isActive = data['isActive'],  user_id = User.objects.get(id=data['user_id']))
        new_bill.save()
        #Loop 'products' field and add a new row in Fact_Prod for each product on the bill
        for pro in data['products']:
            #Add only Foreign Keys on 'ManyToMany' relation, the other fields in Fact_Prod table remain 0
            product_obj = Product.objects.get(product_name = pro['product_name'])
            new_bill.products.add(product_obj)
            #This is a query that fills the other fields on the Fact_Prod table
            Fact_prod.objects.filter(product_id = product_obj.id_product, bill_id = new_bill.id_bill).update(product_amount = pro['product_amount'], sub_total_price = product_obj.product_price * pro['product_amount'] )
        serializer = BillSerializer(new_bill)
        return Response(serializer.data)