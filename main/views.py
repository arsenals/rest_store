from rest_framework.generics import ListAPIView, RetrieveAPIView

from .models import Product
from .serializers import ProductSerializer, ProductDetailsSerializer


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


class ProductDetails(RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductDetailsSerializer



    # {"id": 1, "title": "...", "description": "...",
    #  "price": 29.19, "image": "http://....", "category": {"name": "...", "slug": "..."}}
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

#TODO: CRUD (для продуктов)
#TODO: пагинация
#TODO: фильтрация
#TODO: поиск
#TODO: управление правами доступа
#TODO: корзина
#TODO: оформление заказа