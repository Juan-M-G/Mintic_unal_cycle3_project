from factura.models.fact_prod import Fact_prod
from rest_framework import serializers

class Fact_prodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fact_prod
        fields = ['id_fp', 'bill_id', 'product_id', 'product_amount', 'sub_total_price']
