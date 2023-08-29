from django.contrib import admin
from products.models import *

# Register your models here.
class product_admin(admin.ModelAdmin):
    list_display = ('name','description', 'code', 'price')

admin.site.register(product,product_admin)