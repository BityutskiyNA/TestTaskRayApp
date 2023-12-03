from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView

from products.models import Product

from products.serializers import ProductDetailSerializer, ProductsListSerializer, ProductCreateSerializer, \
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
