from django.contrib import admin
from orders.models import *

# Register your models here.
class order_admin(admin.ModelAdmin):
    list_display = ('id','date', 'code')

class order_product_admin(admin.ModelAdmin):
    list_display = ('id_order', 'quantity', 'id_product')

admin.site.register(order,order_admin)
admin.site.register(order_product,order_product_admin)