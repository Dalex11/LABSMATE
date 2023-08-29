from django.db import models
from products.models import *
from django.contrib.auth.models import User

# Create your models here.
class order(models.Model):

    date= models.DateTimeField(auto_now_add=False, default=None, null=False)
    code= models.BigIntegerField(default=None, null=False, unique=True)
    id_user = models.ForeignKey(User, on_delete=models.CASCADE,null=False,related_name='id_user_in_order')
    # id_order_product= models.ManyToManyField(product, through='order_product')

    class Meta:
        db_table = "order"

class order_product(models.Model):

    id_order= models.ForeignKey(order,on_delete=models.CASCADE,null=False,related_name='id_order_in_order_product')
    quantity= models.IntegerField(default=None, null=False)
    id_product= models.ForeignKey(product,on_delete=models.CASCADE,null=False,related_name='id_product_in_order_product')

    class Meta:
        db_table = "order_product"