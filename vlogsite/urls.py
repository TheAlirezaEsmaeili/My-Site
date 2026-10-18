"""پیکربندی URLهای اصلی پروژه."""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularSwaggerView,
    SpectacularRedocView,
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("blog.urls")),
    path("blog/api/v1/", include("blog.api.v1.urls")),
    path("accounts/",include('accounts.urls')),

    path('api/schema/',SpectacularAPIView.as_view(), name='schema'),
    path('swagger/',SpectacularSwaggerView.as_view(url_name='schema'),name='swagger-ui'),
    path('redoc/',SpectacularRedocView.as_view(url_name='schema'),name='redoc'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
