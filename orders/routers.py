from rest_framework.routers import DefaultRouter
from orders.views import *

router = DefaultRouter()

router.register(r'order', order_viewsets, basename = 'order')
router.register(r'order_product', order_product_viewsets, basename = 'order_product')

urlpatterns = router.urls