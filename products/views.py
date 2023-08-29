from django.shortcuts import render
from products.models import *
from products.serializers import  *
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

# Create your views here.
class product_viewsets (viewsets.ModelViewSet):

    serializer_class = product_serializer
    permission_classes = (IsAuthenticated,)
    queryset = product_serializer.Meta.model.objects.all()