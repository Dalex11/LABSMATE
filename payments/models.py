from django.db import models
from orders.models import order

# Create your models here.
class payment(models.Model):

    date= models.DateTimeField(auto_now_add=False, default=None, null=False)
    method= models.CharField(max_length=100, null=False, default=None)
    pay= models.BigIntegerField(default=None, null=False)

    class Meta:
        db_table = "payment"

class order_payment(models.Model):

    id_order= models.ForeignKey(order,on_delete=models.CASCADE,null=False,related_name='id_order_in_order_payment')
    id_payment= models.ForeignKey(payment,on_delete=models.CASCADE,null=False,related_name='id_payment_in_order_payment')

    class Meta:
        db_table = "order_payment"