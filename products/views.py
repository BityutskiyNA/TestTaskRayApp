from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from django.views.generic import DetailView, CreateView, ListView, UpdateView, DeleteView

from products.models import Product


class ProductListView(LoginRequiredMixin, ListView):
    model = Product


class ProductDetailView(LoginRequiredMixin, DetailView):
    model = Product


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


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    success_url = reverse_lazy('products:index')
