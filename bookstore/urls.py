"""
URL configuration for bookstore project.
"""

from django.conf import settings
from django.contrib import admin
from django.urls import include, path, re_path
from rest_framework.routers import DefaultRouter

from product.views import ProductViewSet

# Crie o router
router = DefaultRouter()
router.register(r"products", ProductViewSet, basename="product")

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include(router.urls)),  # Inclui todas as URLs da API
    path("api-auth/", include("rest_framework.urls")),  # Para autenticação da API
    re_path("bookstore/(?P<version>(v1|v2))/", include("order.urls")),
    re_path("bookstore/(?P<version>(v1|v2))/", include("product.urls")),
]

# Configuração do debug_toolbar apenas em desenvolvimento
if settings.DEBUG and hasattr(settings, 'INSTALLED_APPS'):
    try:
        import debug_toolbar
        if 'debug_toolbar' in settings.INSTALLED_APPS:
            urlpatterns += [
                path('__debug__/', include(debug_toolbar.urls)),
            ]
    except (ImportError, AttributeError):
        pass