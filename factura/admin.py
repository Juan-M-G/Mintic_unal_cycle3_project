from django.contrib import admin
from .models.user import User
from .models.bill import Bill
from .models.fact_prod import Fact_prod
from .models.product import Product

admin.site.register(User)
admin.site.register(Fact_prod)
admin.site.register(Product)
admin.site.register(Bill)
