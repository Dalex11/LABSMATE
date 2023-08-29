from django.urls import path
from payments.views import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'payment', payment_viewsets, 'payment')
router.register(r'order_payment', order_payment_viewsets, 'order_payment')

urlpatterns = [
    path('', payment_viewsets.as_view(), name='payment'),
    path('order_payment/', order_payment_viewsets.as_view(), name='order_payment'),
]