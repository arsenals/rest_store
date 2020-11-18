from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from main.views import ProductsList

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('', ProductsList.as_view())
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
