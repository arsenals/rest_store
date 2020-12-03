from rest_framework import viewsets, generics
from rest_framework.decorators import action
from rest_framework.response import Response

from cart.serializers import CartSerializer, ProductSerializer
from main.models import Cart, Product


class CartViewSet(viewsets.ModelViewSet):
    model = Cart
    serializer_class = CartSerializer

    def get_queryset(self,):
        return Cart.objects.filter(user=self.request.user)


class ProductDetail(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer



class AddProduct(ProductDetail, viewsets.ModelViewSet):
    @action(detail=True)
    def add(self, request, pk):
        cart_obj = Cart.objects.get_or_new(request)
        product_id = pk
        qs = Product.objects.filter(id=product_id)
        if qs.count() == 1:
            product_obj = qs.first()
            if product_obj not in cart_obj.products.all():
                cart_obj.products.add(product_obj)
            else:
                cart_obj.products.remove(product_obj)
            request.session['cart_items'] = cart_obj.products.count()
        return Response({"success":True})
