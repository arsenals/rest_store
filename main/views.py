from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Product
from .serializers import ProductSerializer


# @api_view(['GET'])
# def products_list(request):
#     products = Product.objects.all()
#     serializer = ProductSerializer(products, many=True, context={'request': request})
#     return Response(serializer.data)
#
#
# class ProductsList(APIView):
#     def get(self, request, format=None):
#         products = Product.objects.all()
#         serializer = ProductSerializer(products, many=True, context={'request': request})
#         return Response(serializer.data)

class ProductsList(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    # obj -> {} -> '{}'
    #
    # '{}' -> {} -> obj

    # 'GET', 'POST', 'PATCH', 'PUT', 'DELETE'

    # /products/ "GET" - получение листинга
    # /products/<id>/ "GET" - получение деталей продукта
    # /products/ "POST" - создание продукта
    # /products/<id>/ "PUT/PATCH" - изменение
    # /products/<id>/ "DELETE" - удаление

    # CRUD(Create, Retrieve, Update, Delete)

# {'id': 1, "title": "Adidas Predator", "description": "Brand new cleats"}
# /products/1/ - PUT "{'title': 'Adidas Predator Accelerator'}" -> {'title': 'Adidas Predator Accelerator'}
# /product/1/ - PATCH "{'title': 'Adidas Predator Accelerator'}" -> {'id': 1, "title": "Adidas Predator Accelerator", "description": "Brand new cleats"}
#
# Product() -> {'id': 1, 'title': 'Adidas Originals', ....}
