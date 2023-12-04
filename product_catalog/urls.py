from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("products.urls", namespace="products")),
    path("users/", include("users.urls", namespace="users")),
    path("doc/schema", SpectacularAPIView.as_view(), name="schema"),
    path("doc/schema/swagger-ui/", SpectacularSwaggerView.as_view(url_name="schema")),
]
