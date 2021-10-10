from django.conf import settings
from rest_framework import generics
from factura.models.product import Product
from factura.serializers.productSerializer import ProductSerializer
from rest_framework.permissions import IsAuthenticated

class ProductDetailView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (IsAuthenticated,)