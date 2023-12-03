from django.urls import path

from .api.v1.api_views import APIProductListView, APIProductCreateView, APIProductUpdateView, APIProductDetailView, \
    APIProductDeleteView
from .apps import ProductsConfig
from .views import ProductDetailView, ProductListView, ProductCreateView, ProductUpdateView, ProductDeleteView, \
    ImageUpdateView

app_name = ProductsConfig.name

urlpatterns = [
    path('', ProductListView.as_view(), name='index'),
    path('create/', ProductCreateView.as_view(), name='create'),
    path('update/<int:pk>/', ProductUpdateView.as_view(), name='update'),
    path('view/<int:pk>/', ProductDetailView.as_view(), name='view'),
    path('delete/<int:pk>/', ProductDeleteView.as_view(), name='delete'),
    path('image/', ImageUpdateView.as_view(), name='image'),
    path('api/', APIProductListView.as_view(), name='APIListView'),
    path('api/create/', APIProductCreateView.as_view(), name='APIProductCreate'),
    path('api/<int:pk>/update/', APIProductUpdateView.as_view(), name='APIProductUpdate'),
    path('api/<int:pk>/view/', APIProductDetailView.as_view(), name='APIProductDetail'),
    path('api/<int:pk>/delete/', APIProductDeleteView.as_view(), name='APIProductDelete'),
]
