from django.urls import path
from shipments.views import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'shipment', shipment_viewsets, 'shipment')
router.register(r'order_shipment', order_shipment_viewsets, 'order_shipment')

urlpatterns = [
    path('', order_shipment_viewsets.as_view(), name='order_shipment'),
]