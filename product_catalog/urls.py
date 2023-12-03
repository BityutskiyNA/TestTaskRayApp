from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('api-auth/', include('rest_framework.urls')),
    path('', include('products.urls', namespace='products')),
    path('users/', include('users.urls', namespace='users')),

]
