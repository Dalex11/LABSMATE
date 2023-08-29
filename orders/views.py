from django.shortcuts import render
from orders.models import *
from orders.serializers import  *
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework import status

# Create your views here.
class order_viewsets (viewsets.ModelViewSet):

    serializer_class = order_serializer
    permission_classes = (IsAuthenticated,)
    queryset = order_serializer.Meta.model.objects.all()

class order_product_viewsets (viewsets.ModelViewSet):

    serializer_class = order_product_serializer
    permission_classes = (IsAuthenticated,)
    queryset = order_product_serializer.Meta.model.objects.all()

# class add_product_order_viewsets (APIView):
#     def post(self, request, order_id, product_id):
#         try:
#             current_order = order.objects.get(id=order_id)
#             selected_product = product.objects.get(id=product_id)  # Asegúrate de importar el modelo 'product'
#         except order.DoesNotExist or product.DoesNotExist:
#             return Response({"message": "Order or Product not found"}, status=status.HTTP_404_NOT_FOUND)
        
#         quantity = request.data.get('quantity')
        
#         if quantity is None:
#             return Response({"message": "Quantity is required"}, status=status.HTTP_400_BAD_REQUEST)
        
#         order_product_obj = order_product.objects.create(
#             id_order=current_order,
#             id_product=selected_product,
#             quantity=quantity
#         )
        
#         serializer = order_product_serializer(order_product_obj)
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
    
#     def delete(self, request, order_product_id):
#         try:
#             order_product_obj = order_product.objects.get(id=order_product_id)
#         except order_product.DoesNotExist:
#             return Response({"message": "Order Product not found"}, status=status.HTTP_404_NOT_FOUND)
        
#         order_product_obj.delete()
        
#         return Response({"message": "Order Product deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
    
#     def put(self, request, order_product_id):
#         try:
#             order_product_obj = order_product.objects.get(id=order_product_id)
#         except order_product.DoesNotExist:
#             return Response({"message": "Order Product not found"}, status=status.HTTP_404_NOT_FOUND)
        
#         new_quantity = request.data.get('quantity')
        
#         if new_quantity is None:
#             return Response({"message": "Quantity is required"}, status=status.HTTP_400_BAD_REQUEST)
        
#         order_product_obj.quantity = new_quantity
#         order_product_obj.save()
        
#         return Response({"message": "Quantity updated successfully"}, status=status.HTTP_200_OK)