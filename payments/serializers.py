from rest_framework import serializers
from payments.models import *

class payment_serializer(serializers.ModelSerializer):
	class Meta:
		model = payment
		fields = '__all__'

class order_payment_serializer(serializers.ModelSerializer):
	class Meta:
		model = order_payment
		fields = '__all__'