from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_swagger.views import get_swagger_view
from main.views import ProductViewSet, CommentViewSet

from cart.views import OrdersViewSet


router = DefaultRouter()
router.register('products', ProductViewSet)
router.register(r'cart', OrdersViewSet)
router.register(r'comments', CommentViewSet)

schema_view = get_swagger_view(title="EMS API Documentation")

urlpatterns = [
    path('api_documentation/', schema_view),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('accounts/', include('account.urls')),
    path('', include(router.urls))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)