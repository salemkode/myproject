from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin

from products.models import Product


class ProductListView(LoginRequiredMixin, ListView):
    model = Product
    template_name = "products/product_list.html"
    context_object_name = "products"


class ProductDetailView(LoginRequiredMixin, DetailView):
    model = Product
    template_name = "products/product_detail.html"
    context_object_name = "product"


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    template_name = "products/product_form.html"
    fields = ['name', 'description', 'price', 'stock']
    success_url = "/products/"


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    template_name = "products/product_form.html"
    fields = ['name', 'description', 'price', 'stock']
    success_url = "/products/"


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    template_name = "products/product_confirm_delete.html"
    success_url = "/products/"
