from django.db import models
from orders.models import order

# Create your models here.
class shipment(models.Model):

    date= models.DateTimeField(auto_now_add=False, default=None, null=False)
    address= models.CharField(max_length=100, null=False, default=None)
    city= models.CharField(max_length=100, null=False, default=None)
    department= models.CharField(max_length=100, null=False, default=None)
    country= models.CharField(max_length=100, null=False, default=None)
    code= models.BigIntegerField(default=None, null=False, unique=True)
    state= models.CharField(max_length=100, null=False, default=None)

    class Meta:
        db_table = "shipment"

class order_shipment(models.Model):

    id_order= models.ForeignKey(order,on_delete=models.CASCADE,null=False,related_name='id_order_in_order_shipment')
    id_shipment= models.ForeignKey(shipment,on_delete=models.CASCADE,null=False,related_name='id_shipment_in_order_shipment')

    class Meta:
        db_table = "order_shipment"