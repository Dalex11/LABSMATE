from django.shortcuts import render
from shipments.models import *
from shipments.serializers import  *
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.decorators import permission_required

# Create your views here.
class shipment_viewsets (viewsets.ModelViewSet):

    serializer_class = shipment_serializer
    permission_classes = (IsAuthenticated,)
    queryset = shipment_serializer.Meta.model.objects.all()

class order_shipment_viewsets (viewsets.ModelViewSet):

    serializer_class = shipment_serializer
    permission_classes = (IsAuthenticated,)
    queryset = shipment_serializer.Meta.model.objects.all()