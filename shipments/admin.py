from django.contrib import admin
from shipments.models import *

# Register your models here.
class shipment_admin(admin.ModelAdmin):
    list_display = ('id','date', 'address', 'city', 'department','country', 'code', 'state')

class order_shipment_admin(admin.ModelAdmin):
    list_display = ('id_order', 'id_shipment')

admin.site.register(shipment,shipment_admin)
admin.site.register(order_shipment,order_shipment_admin)