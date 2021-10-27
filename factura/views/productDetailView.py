from rest_framework import generics
from factura.models.product import Product
from factura.serializers.productSerializer import ProductSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

class ProductDetailView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (IsAuthenticated,)
    #Update feature applied to Product table across PUT method, according to Rest_Framework
    def put(self, request, pk = None):
        product = Product.objects.filter(id_product = pk).first()
        product_serializer = ProductSerializer(product, data = request.data)
        if product_serializer.is_valid():
            product_serializer.save()
            return Response(product_serializer.data)
        return Response(product_serializer.errors)