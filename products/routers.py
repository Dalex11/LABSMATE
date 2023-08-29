from rest_framework.routers import DefaultRouter
from products.views import *

router = DefaultRouter()

router.register(r'product', product_viewsets, basename = 'product')

urlpatterns = router.urls