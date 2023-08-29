from django.urls import path
from orders.views import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'order', order_viewsets, 'order')
router.register(r'order_product', order_product_viewsets, 'order_product')

urlpatterns = [
    path('', order_viewsets.as_view(), name='order'),
    path('order_product/', order_product_viewsets.as_view(), name='order_product'),
    path('add_product_order/<int:order_id>/<int:product_id>/', add_product_order.as_view(), name='add_product_order'),
]