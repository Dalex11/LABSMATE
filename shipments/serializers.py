from rest_framework import serializers
from shipments.models import *

class shipment_serializer(serializers.ModelSerializer):
	class Meta:
		model = shipment
		fields = '__all__'
		
class order_shipment_serializer(serializers.ModelSerializer):
	class Meta:
		model = order_shipment
		fields = '__all__'