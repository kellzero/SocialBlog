from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import redirect
from product.views import ProductViewSet
from bookstore import views  # 👈 Importação correta do views

def home(request):
    return redirect('/login/')

router = DefaultRouter()
router.register(r"products", ProductViewSet, basename="product")

urlpatterns = [
    path('login/', TemplateView.as_view(template_name='index.html'), name='login'),
    path('feed/', TemplateView.as_view(template_name='feed.html'), name='feed'),

    path('', home),  # Página inicial
    path('admin/', admin.site.urls),
    path('hello/', views.hello_world, name='hello_world'),  # Agora views existe
    path('update_server/', views.update_server, name='update_server'),
    path("api/", include(router.urls)),
    path("api-auth/", include("rest_framework.urls")),
    path('api/accounts/', include('accounts.urls')),
    path('api/posts/', include('posts.urls')),
    path('perfil/', TemplateView.as_view(template_name='perfil.html'), name='perfil'),
    re_path("bookstore/(?P<version>(v1|v2))/", include("order.urls")),
    re_path("bookstore/(?P<version>(v1|v2))/", include("product.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    try:
        import debug_toolbar
        urlpatterns += [
            path('__debug__/', include(debug_toolbar.urls)),
        ]
    except ImportError:
        pass
