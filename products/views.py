from http import HTTPStatus

from asgiref.sync import sync_to_async
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.core.cache import cache
from django.views.generic import DetailView, CreateView, ListView, UpdateView, DeleteView

from product_catalog import settings
from products.models import Product
from products.services import save_photos


class ProductListView(LoginRequiredMixin, ListView):
    model = Product


class ProductDetailView(LoginRequiredMixin, DetailView):
    model = Product

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        if settings.CACHES_ENABLED:
            key = f"images_list_{self.object.pk}"
            images_list = cache.get(key)
            if images_list is None:
                images_list = self.object.images.all()
                cache.set(key, images_list)
        else:
            images_list = self.object.images.all()
        context_data['images'] = images_list
        return context_data


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    fields = ('name', 'article', 'description', 'description'
              , 'product_type', 'price', 'quantity', 'images')
    success_url = reverse_lazy('products:index')


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    fields = ('name', 'article', 'description', 'description'
              , 'product_type', 'price', 'quantity', 'images')
    success_url = reverse_lazy('products:index')


class ProductDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Product
    success_url = reverse_lazy('products:index')
    permission_required = 'products.delite.product'


@method_decorator(csrf_exempt, name='dispatch')
class ImageUpdateView(View):
    @sync_to_async
    def get_product_names_list(self):
        return list(Product.objects.filter(images__link__isnull=True).values('id', 'name'))

    async def post(self, request, *args, **kwargs):
        search_queries = await self.get_product_names_list()

        images = await save_photos(search_queries)

        return HttpResponse(status=HTTPStatus.OK)
