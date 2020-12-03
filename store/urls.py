from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

# from main.views import ProductsList, ProductDetails, CreateProduct, UpdateProduct, DeleteProduct
from rest_framework.routers import DefaultRouter

from main.views import ProductViewSet


router = DefaultRouter()
router.register('products', ProductViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('accounts/', include('account.urls')),
    path('', include(router.urls))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
