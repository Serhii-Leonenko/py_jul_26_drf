from debug_toolbar.toolbar import debug_toolbar_urls
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)

urlpatterns = (
    [
        path("admin/", admin.site.urls),
        path("api-auth/", include("rest_framework.urls")),
        path("", include("messenger.urls")),
        path("", include("users.urls")),
        # docs
        path("schema/", SpectacularAPIView.as_view(), name="schema"),
        path(
            "docs/redoc/", SpectacularRedocView.as_view(url_name="schema"), name="redoc"
        ),
        path(
            "docs/", SpectacularSwaggerView.as_view(url_name="schema"), name="swagger"
        ),
    ]
    + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    + debug_toolbar_urls()
)
