from django.conf import settings
from rest_framework import generics, status
from rest_framework.response import Response
from factura.models.bill import Bill
from factura.serializers.billSerializer import BillSerializer
from rest_framework.permissions import IsAuthenticated

class BillDetailView(generics.RetrieveAPIView):
    queryset = Bill.objects.all()
    serializer_class = BillSerializer
    permission_classes = (IsAuthenticated,)

#    def get(self, request, *args, **kwargs):
#        token = request.META.get('HTTP_AUTHORIZATION')[7:]
#        tokenBackend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
#        valid_data = tokenBackend.decode(token,verify=False)
#        if valid_data['user_id'] != kwargs['pk']:
#            stringResponse = {'detail':'Unauthorized Request'}
#            return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED)
#        return super().get(request, *args, **kwargs)