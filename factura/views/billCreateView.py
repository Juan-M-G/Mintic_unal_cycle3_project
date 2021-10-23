from rest_framework import status, views
from rest_framework.response import Response
from factura.serializers.billSerializer import BillSerializer
from factura.models import Bill, Product, User, Fact_prod


class BillCreateView(views.APIView):
#    def post(self, request, *args, **kwargs):
#        serializer = BillSerializer(data=request.data)
#        serializer.is_valid(raise_exception=True)
#        serializer.save()
#        return Response("Added new bill", status=status.HTTP_201_CREATED)

#from django.contrib.auth.models import User
#MyModel.objects.filter(pk=some_value).update(field1='some value')
#staffprofile.user = user

    def post(self, request, *args, **kwargs):
        data = request.data
        new_bill = Bill.objects.create(client_name = data['client_name'], purchase_Date = data['purchase_Date'], isActive = data['isActive'],  user_id = User.objects.get(id=data['user_id']))
        
        new_bill.save()
        for pro in data['products']:
            product_obj = Product.objects.get(product_name = pro['product_name'])
            new_bill.products.add(product_obj)
            Fact_prod.objects.filter(product_id = product_obj.id_product ).update(product_amount = pro['product_amount'], sub_total_price = product_obj.product_price * pro['product_amount'] )
        serializer = BillSerializer(new_bill)
        return Response(serializer.data, product_obj.product_price)