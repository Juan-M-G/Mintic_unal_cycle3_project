from rest_framework import generics
from rest_framework.response import Response
from factura.models.bill import Bill
from factura.serializers.billSerializer import BillSerializer
from rest_framework.permissions import IsAuthenticated

class DailySellsDetailView(generics.RetrieveAPIView):
    #permission_classes = (IsAuthenticated,)
    queryset = Bill.objects.all()
    def get(self, request, *args, **kwargs):
        bills = Bill.objects.all()
        serializer_class = BillSerializer(bills, many = True)
        return Response(serializer_class.data)


