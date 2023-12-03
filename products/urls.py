from django.contrib import admin
from django.urls import path, include

from .apps import ProductsConfig
from .views import ProductDetailView, ProductListView, ProductCreateView, ProductUpdateView, ProductDeleteView

app_name = ProductsConfig.name

urlpatterns = [
    path('', ProductListView.as_view(), name='index'),
    path('create/', ProductCreateView.as_view(), name='create'),
    path('update/<int:pk>/', ProductUpdateView.as_view(), name='update'),
    path('view/<int:pk>/', ProductDetailView.as_view(), name='view'),
    path('delete/<int:pk>/', ProductDeleteView.as_view(), name='delete'),
]
