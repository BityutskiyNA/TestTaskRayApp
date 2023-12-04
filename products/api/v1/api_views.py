from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
    CreateAPIView,
    UpdateAPIView,
    DestroyAPIView,
)

from products.models import Product

from products.serializers import (
    ProductDetailSerializer,
    ProductsListSerializer,
    ProductCreateSerializer,
    ProductUpdateSerializer,
    ProductDestroySerializer,
)


class APIProductListView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductsListSerializer


class APIProductDetailView(RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductDetailSerializer


class APIProductCreateView(CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductCreateSerializer


class APIProductUpdateView(UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductUpdateSerializer


class APIProductDeleteView(DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductDestroySerializer
