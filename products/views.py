from django.http import JsonResponse
from django.shortcuts import render
from django.views import View
from django.views.generic import DetailView
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView

from products.models import Product
from .serializers import ProductDetailSerializer, ProductsListSerializer, ProductCreateSerializer, \
    ProductUpdateSerializer, ProductDestroySerializer


class ProductListView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductsListSerializer


class ProductDetailView(RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductDetailSerializer


class ProductCreateView(CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductCreateSerializer


class ProductUpdateView(UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductUpdateSerializer

class ProductDeleteView(DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductDestroySerializer
