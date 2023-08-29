from django.contrib import admin
from payments.models import *

# Register your models here.
class payment_admin(admin.ModelAdmin):
    list_display = ('id','date', 'method', 'pay')

class order_payment_admin(admin.ModelAdmin):
    list_display = ('id_order','id_payment')

admin.site.register(payment,payment_admin)
admin.site.register(order_payment,order_payment_admin)