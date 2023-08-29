from django.db import models

# Create your models here.
class product(models.Model):

    name= models.CharField(max_length=100, null=False, default=None)
    description= models.CharField(max_length=500, null=False, default=None)
    code= models.BigIntegerField(default=None, null=False, unique=True)
    price= models.BigIntegerField(default=None, null=False)

    class Meta:
        db_table = "product"