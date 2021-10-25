from rest_framework import generics
from factura.models import bill
from factura.models.bill import Bill
from factura.serializers.billSerializer import BillSerializer
from rest_framework.permissions import IsAuthenticated

class DailySellsDetailView(generics.RetrieveAPIView):
    queryset = Bill.objects.all()
    serializer_class = BillSerializer(bill, many = True)
    permission_classes = (IsAuthenticated,)
    


