from django.shortcuts import render
from payments.models import *
from payments.serializers import  *
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from django.http import HttpResponse
import csv

# Create your views here.
class payment_viewsets (viewsets.ModelViewSet):

    serializer_class = payment_serializer
    #permission_classes = (IsAuthenticated,)
    queryset = payment_serializer.Meta.model.objects.all()

class order_payment_viewsets (viewsets.ModelViewSet):

    serializer_class = order_payment_serializer
    permission_classes = (IsAuthenticated,)
    queryset = order_payment_serializer.Meta.model.objects.all()