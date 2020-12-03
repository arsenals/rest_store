from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.viewsets import ModelViewSet

from .filters import ProductFilter
from .models import Product
from .permisssions import ProductPermission
from .serializers import ProductSerializer, ProductDetailsSerializer, CreateProductSerializer, UpdateProductSerializer

class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductDetailsSerializer
    filterset_class = ProductFilter

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            permissions = []
        else:
            permissions = [ProductPermission, ]
        return [permission() for permission in permissions]
