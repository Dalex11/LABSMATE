from rest_framework import serializers
from orders.models import *

class order_serializer(serializers.ModelSerializer):
	class Meta:
		model = order
		fields = '__all__'

class order_product_serializer(serializers.ModelSerializer):
	class Meta:
		model = order_product
		fields = '__all__'