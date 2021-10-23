from rest_framework import status, views
from rest_framework.response import Response
from factura.serializers.billSerializer import BillSerializer
from factura.models import Bill, Product, User


class BillCreateView(views.APIView):
#    def post(self, request, *args, **kwargs):
#        serializer = BillSerializer(data=request.data)
#        serializer.is_valid(raise_exception=True)
#        serializer.save()
#        return Response("Added new bill", status=status.HTTP_201_CREATED)

#from django.contrib.auth.models import User

#staffprofile.user = user

    def post(self, request, *args, **kwargs):
        data = request.data
        new_bill = Bill.objects.create(client_name = data['client_name'], purchase_Date = data['purchase_Date'], isActive = data['isActive'],  user_id = User.objects.get(id=data['user_id']))
        
        new_bill.save()
        for pro in data['products']:
            product_obj = Product.objects.get(product_name = pro['product_name'])
            
            new_bill.products.add(product_obj)
        serializer = BillSerializer(new_bill)
        return Response(product_obj.product_price)