from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from crm_system.mixins import CustomPermissionRequiredMixin
from .models import Product


# Create your views here.
class ProductsListView(CustomPermissionRequiredMixin, ListView):
    permission_required = 'products.view_product'
    model = Product
    template_name = 'products/products-list.html'
    context_object_name = 'products'

class ProductsDetailView(CustomPermissionRequiredMixin, DetailView):
    permission_required = 'products.view_product'
    model = Product
    template_name = 'products/products-detail.html'

class ProductsCreateView(CustomPermissionRequiredMixin, CreateView):
    permission_required = 'products.add_product'
    model = Product
    fields = ['name', 'description', 'cost']
    template_name = 'products/products-create.html'
    success_url = reverse_lazy('products:products-list')

class ProductsUpdateView(CustomPermissionRequiredMixin, UpdateView):
    permission_required = 'products.change_product'
    model = Product
    fields = ['name', 'description', 'cost']
    template_name = 'products/products-edit.html'
    success_url = reverse_lazy('products:products-list')

class ProductsDeleteView(CustomPermissionRequiredMixin, DeleteView):
    permission_required = 'products.delete_product'
    model = Product
    template_name = 'products/products-delete.html'
    success_url = reverse_lazy('products:products-list')






