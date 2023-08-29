from rest_framework import serializers
from products.models import *

class product_serializer(serializers.ModelSerializer):
	class Meta:
		model = product
		fields = '__all__'