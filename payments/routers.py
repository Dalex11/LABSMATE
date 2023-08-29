from rest_framework.routers import DefaultRouter
from payments.views import *

router = DefaultRouter()

router.register(r'payment', payment_viewsets, basename = 'payment')
router.register(r'order_payment', order_payment_viewsets, basename = 'order_payment')


urlpatterns = router.urls