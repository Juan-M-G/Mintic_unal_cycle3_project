from rest_framework import status, views
from rest_framework.response import Response
from factura.serializers.billSerializer import BillSerializer

class BillCreateView(views.APIView):
    def post(self, request, *args, **kwargs):
        serializer = BillSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response("Added new bill", status=status.HTTP_201_CREATED)