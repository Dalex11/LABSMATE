from django.urls import path
from products.views import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'product', product_viewsets, 'product')

urlpatterns = [
    path('', product_viewsets.as_view(), name='product'),
]