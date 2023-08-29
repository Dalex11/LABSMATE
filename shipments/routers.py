from rest_framework.routers import DefaultRouter
from shipments.views import *

router = DefaultRouter()

router.register(r'shipment', shipment_viewsets, basename = 'shipment')
router.register(r'order_shipment', order_shipment_viewsets, basename = 'order_shipment')

urlpatterns = router.urls