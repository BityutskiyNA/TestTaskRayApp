from django.contrib import admin
from django.urls import path, include
from .views import ProductDetailView, ProductListView, ProductCreateView, ProductUpdateView, ProductDeleteView

urlpatterns = [
    path('', ProductListView.as_view()),
    path('create/', ProductCreateView.as_view()),
    path('<int:pk>/update/', ProductUpdateView.as_view()),
    path('<int:pk>/delete/', ProductDeleteView.as_view()),
    path('<int:pk>/', ProductDetailView.as_view()),
]
