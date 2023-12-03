from rest_framework import serializers

from products.models import Product, Images


class ProductsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'article', 'description',
                  'product_type', 'price']


class ProductDetailSerializer(serializers.ModelSerializer):
    images = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='link'
    )

    class Meta:
        model = Product
        fields = '__all__'


class ProductCreateSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
    images = serializers.SlugRelatedField(
        required=False,
        many=True,
        queryset=Images.objects.all(),
        slug_field='link'
    )

    class Meta:
        model = Product
        fields = '__all__'

    def is_valid(self, *, raise_exception=False):
        self._images = self.initial_data.pop('images')
        return super().is_valid(raise_exception=raise_exception)

    def create(self, validated_data):
        product = Product.objects.create(**validated_data)

        for image in self._images:
            image_obj, _ = Images.objects.get_or_create(link=image)
            product.images.add(image_obj)

        product.save()
        return product


class ProductUpdateSerializer(serializers.ModelSerializer):
    images = serializers.SlugRelatedField(
        required=False,
        many=True,
        queryset=Images.objects.all(),
        slug_field='link'
    )

    class Meta:
        model = Product
        fields = ['id', 'name', 'article', 'description', 'description'
            , 'product_type', 'price', 'quantity', 'images']

    def is_valid(self, *, raise_exception=False):
        self._images = self.initial_data.pop('images')
        return super().is_valid(raise_exception=raise_exception)

    def save(self):
        product = super().save()

        for image in self._images:
            image_obj, _ = Images.objects.get_or_create(link=image)
            product.images.add(image_obj)

        product.save()
        return product


class ProductDestroySerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id']
