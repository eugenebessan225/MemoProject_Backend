
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from ..biblio.urls import router as biblio_router
from rest_framework import routers

router = routers.DefaultRouter()
router.registry.extend(biblio_router.registry)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('router.urls')),
] + + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

