from django.conf import settings
from rest_framework import generics, status
#from rest_framework.response import Response
from factura.models.bill import Bill
from factura.serializers.billSerializer import BillSerializer
from rest_framework.permissions import IsAuthenticated

class BillDetailView(generics.RetrieveAPIView):
    queryset = Bill.objects.all()
    serializer_class = BillSerializer
    permission_classes = (IsAuthenticated,)
